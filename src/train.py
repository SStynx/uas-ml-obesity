import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
import joblib

def train_model_pipeline():
    data_path = 'data/ObesityDataSet_raw_and_data_sinthetic.csv'
    if not os.path.exists(data_path):
        print(f"Error: Berkas dataset tidak ditemukan di {data_path}")
        return
        
    print("[1/6] Membaca dataset mentah...")
    df = pd.read_csv(data_path)
    X = df.drop(columns=['NObeyesdad'])
    y = df['NObeyesdad']
    
    print("[2/6] Memproses Label Encoder Target...")
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    print("[3/6] Mengonversi Fitur Kategorikal (One-Hot Encoding)...")
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    X_encoded = pd.get_dummies(X, columns=categorical_cols)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )
    
    print("[4/6] Menghitung Standarisasi Fitur Numerik...")
    scaler = StandardScaler()
    numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    scaler.fit(X_train[numeric_cols])
    
    X_train_scaled = X_train.copy()
    X_train_scaled[numeric_cols] = scaler.transform(X_train[numeric_cols])
    
    print("[5/6] Melatih Model SVM dengan Parameter Terbaik...")
    best_svm = SVC(C=10, gamma='auto', kernel='rbf', random_state=42)
    best_svm.fit(X_train_scaled, y_train)
    
    
    best_svm.feature_names_in_ = X_train.columns.to_numpy()
    
    print("[6/6] Menyimpan semua biner kompilasi ke folder models/...")
    os.makedirs('models', exist_ok=True)
    joblib.dump(best_svm, 'models/best_obesity_model.joblib')
    joblib.dump(scaler, 'models/scaler.joblib')
    joblib.dump(le, 'models/label_encoder.joblib')
    print(">> Retraining Sukses! Seluruh file .joblib diperbarui.")

if __name__ == "__main__":
    train_model_pipeline()