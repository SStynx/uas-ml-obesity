# Sistem Pakar Prediksi Tingkat Obesitas Berbasis Machine Learning

Aplikasi web end-to-end untuk melakukan skrining awal risiko tingkat obesitas berdasarkan karakteristik demografi, kebiasaan makan, dan gaya hidup. Proyek ini dibangun menggunakan algoritma **Support Vector Machine (SVM)** yang dioptimasikan.

---

## Ringkasan Performa Model
Proyek ini membandingkan 3 algoritma (*K-Nearest Neighbors, Gaussian Naive Bayes,* dan *Support Vector Machine*). Melalui 3 tahapan optimasi (**SMOTE Handling**, **Stratified Cross-Validation**, dan **Hyperparameter Tuning via GridSearchCV**), **SVM** terpilih sebagai model terbaik dengan performa sebagai berikut:

* **Model Terbaik:** Support Vector Machine (SVM)
* **Hyperparameter Optimal:** `{"C": 10, "gamma": "auto", "kernel": "rbf"}`
* **Akurasi Akhir:** **97.12%**
* **Macro-F1 Score:** **97.00%**

---

## Panduan Instalasi dan Cara Menjalankan
1. Prasyarat Awal
    Pastikan komputer Anda sudah terinstal Python 3.9 s.d. Python 3.11. Buka terminal/command prompt di direktori proyek ini, lalu instal seluruh pustaka yang diperlukan:
    pip install -r requirements.txt

2. Menjalankan Aplikasi Web Utama (Streamlit)
    Aplikasi ini menyediakan dasbor interaktif, form kuesioner klinis, dan hasil prediksi yang dilengkapi pernyataan etis data.
    streamlit run app_streamlit.py

3. Fitur Otomatisasi Tambahan (Folder src/)
    * Membuat Data Pasien Acak untuk QA Testing:
        python src/data_generator.py
    * Melakukan Latih Ulang Model (Retraining Pipeline):
        Jika data mentah di folder data/ diperbarui, jalankan perintah ini untuk memperbarui semua file .joblib di folder models/ secara otomatis:
        python src/train.py

## Kontributor & Hak Cipta
Proyek ini disusun dan dikembangkan sebagai pemenuhan syarat penilaian komponen Tugas Akhir / Ujian Akhir Semester (UAS) mata kuliah Machine Learning.