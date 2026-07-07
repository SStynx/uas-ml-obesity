import pandas as pd
import numpy as np
import random
import os

def generate_dummy_patients(num_patients=10, output_path="data/dummy_patients_test.csv"):
    """
    menghasilkan data pasien sintetis / fiktif secara acak
    """
    print(f"Membuat {num_patients} data pasien fiktif...")
    
    dummy_data = {
        'Gender': [random.choice(["Male", "Female"]) for _ in range(num_patients)],
        'Age': [round(random.uniform(14.0, 61.0), 1) for _ in range(num_patients)],
        'Height': [round(random.uniform(1.4, 2.0), 2) for _ in range(num_patients)],
        'Weight': [round(random.uniform(39.0, 173.0), 1) for _ in range(num_patients)],
        'family_history_with_overweight': [random.choice(["yes", "no"]) for _ in range(num_patients)],
        'FAVC': [random.choice(["yes", "no"]) for _ in range(num_patients)],
        'FCVC': [round(random.uniform(1.0, 3.0), 1) for _ in range(num_patients)],
        'NCP': [round(random.uniform(1.0, 4.0), 1) for _ in range(num_patients)],
        'CAEC': [random.choice(["no", "Sometimes", "Frequently", "Always"]) for _ in range(num_patients)],
        'SMOKE': [random.choice(["yes", "no"]) for _ in range(num_patients)],
        'CH2O': [round(random.uniform(1.0, 3.0), 1) for _ in range(num_patients)],
        'SCC': [random.choice(["yes", "no"]) for _ in range(num_patients)],
        'FAF': [round(random.uniform(0.0, 3.0), 1) for _ in range(num_patients)],
        'TUE': [round(random.uniform(0.0, 2.0), 1) for _ in range(num_patients)],
        'CALC': [random.choice(["no", "Sometimes", "Frequently", "Always"]) for _ in range(num_patients)],
        'MTRANS': [random.choice(["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"]) for _ in range(num_patients)]
    }
    
    # Bungkus menjadi DataFrame
    df_dummy = pd.DataFrame(dummy_data)
    
    # Simpan ke dalam folder data/
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_dummy.to_csv(output_path, index=False)
    
    print(f"Berhasil! Data uji berhasil disimpan di: {output_path}")
    return df_dummy

if __name__ == "__main__":
    
    generate_dummy_patients(20)