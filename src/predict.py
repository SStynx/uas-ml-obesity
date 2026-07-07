import joblib
import pandas as pd
from src.ml_core import MAP_TARGET

def predict_obesity_risk(raw_input_df):
    """
    Melakukan pipeline transformasi data (One-Hot Encoding, Reindexing, Scaling)
    dan mengembalikan hasil prediksi akhir dalam bentuk teks Bahasa Indonesia.
    """
    # 1. Memuat model dan komponen biner pendukung dari folder models/
    model = joblib.load('models/best_obesity_model.joblib')
    scaler = joblib.load('models/scaler.joblib')
    encoder = joblib.load('models/label_encoder.joblib')
    
    # 2. Melakukan One-Hot Encoding pada fitur kategorikal
    categorical_cols = ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS']
    input_encoded = pd.get_dummies(raw_input_df, columns=categorical_cols)
    
    # 3. Menyelaraskan kolom dengan matriks data training
    model_features = model.feature_names_in_
    input_ready = input_encoded.reindex(columns=model_features, fill_value=0)
    
    # 4. Feature Scaling pada kolom numerik asli
    numeric_cols = scaler.feature_names_in_
    input_ready[numeric_cols] = scaler.transform(input_ready[numeric_cols])
    
    # 5. Inferensi Evaluasi Model AI
    prediction_numeric = model.predict(input_ready)
    
    # 6. Menerjemahkan angka kembali ke label string asal
    prediction_string = encoder.inverse_transform(prediction_numeric)[0]
    
    # 7. Mengembalikan teks luaran
    clean_text = prediction_string.replace('_', ' ')
    return MAP_TARGET.get(clean_text, clean_text)