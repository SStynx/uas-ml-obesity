import pandas as pd

# Kamus Pemetaan Bahasa Indonesia ke Bahasa Inggris (Sesuai Dataset Asli)
MAP_YESNO = {"Ya": "yes", "Tidak": "no"}
MAP_FREQ = {"Tidak Pernah": "no", "Kadang-kadang": "Sometimes", "Sering": "Frequently", "Selalu": "Always"}
MAP_TRANS = {
    "Transportasi Umum": "Public_Transportation", 
    "Mobil Pribadi": "Automobile", 
    "Jalan Kaki": "Walking", 
    "Sepeda Motor": "Motorbike", 
    "Sepeda": "Bike"
}


MAP_TARGET = {
    "Insufficient Weight": "Kekurangan Berat Badan",
    "Normal Weight": "Berat Badan Normal",
    "Overweight Level I": "Kelebihan Berat Badan (Level I)",
    "Overweight Level II": "Kelebihan Berat Badan (Level II)",
    "Obesity Type I": "Obesitas (Tipe I)",
    "Obesity Type II": "Obesitas (Tipe II)",
    "Obesity Type III": "Obesitas Ekstrem (Tipe III)"
}

def preprocess_ui_input(inputs_ui):
    """
    Mengonversi input dari User Interface (Bahasa Indonesia) ke format DataFrame 
    berbahasa Inggris yang sesuai dengan karakteristik dataset asli.
    """
    gender = "Male" if inputs_ui['gender'] == "Laki-laki" else "Female"
    
    raw_input = pd.DataFrame({
        'Gender': [gender],
        'Age': [inputs_ui['age']],
        'Height': [inputs_ui['height']],
        'Weight': [inputs_ui['weight']],
        'family_history_with_overweight': [MAP_YESNO[inputs_ui['family_history']]],
        'FAVC': [MAP_YESNO[inputs_ui['favc']]],
        'FCVC': [inputs_ui['fcvc']],
        'NCP': [inputs_ui['ncp']],
        'CAEC': [MAP_FREQ[inputs_ui['caec']]],
        'SMOKE': [MAP_YESNO[inputs_ui['smoke']]],
        'CH2O': [inputs_ui['ch2o']],
        'SCC': [MAP_YESNO[inputs_ui['scc']]],
        'FAF': [inputs_ui['faf']],
        'TUE': [inputs_ui['tue']],
        'CALC': [MAP_FREQ[inputs_ui['calc']]],
        'MTRANS': [MAP_TRANS[inputs_ui['mtrans']]]
    })
    
    return raw_input