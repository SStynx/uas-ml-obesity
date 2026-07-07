import streamlit as st
from src.ml_core import preprocess_ui_input
from src.predict import predict_obesity_risk

# Konfigurasi Tampilan
st.set_page_config(page_title="Prediktor Risiko Obesitas", layout="centered", page_icon="🩺")

st.title("🩺 Sistem Pakar Prediksi Tingkat Obesitas")
st.caption("Aplikasi Skrining Awal Berbasis Machine Learning")
st.warning(
    "⚠️ **Pernyataan Etis & Privasi Data:** Aplikasi ini hanya digunakan untuk tujuan edukasi "
    "dan skrining awal. Hasil prediksi tidak boleh dijadikan sebagai keputusan medis tunggal."
)
st.markdown("---")

st.header("📝 Form Kuesioner Klinis & Gaya Hidup")
with st.form("obesity_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Umur (Tahun)", min_value=14, max_value=61, value=25)
        height = st.number_input("Tinggi Badan (Meter)", min_value=1.4, max_value=2.0, value=1.70, step=0.01)
        weight = st.number_input("Berat Badan (Kg)", min_value=39.0, max_value=173.0, value=70.0, step=0.1)
        gender_ui = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
        family_history_ui = st.selectbox("Ada Riwayat Obesitas pada Keluarga?", ["Ya", "Tidak"])
        favc_ui = st.selectbox("Sering Jamu Makanan Tinggi Kalori? (Junk Food)", ["Ya", "Tidak"])
        smoke_ui = st.selectbox("Apakah Anda Merokok?", ["Ya", "Tidak"])
        scc_ui = st.selectbox("Apakah Anda Rutin Menghitung Kalori Harian?", ["Tidak", "Ya"])
    with col2:
        fcvc = st.slider("Frekuensi Makan Sayur (1: Jarang, 3: Selalu)", 1.0, 3.0, 2.0, step=0.1)
        ncp = st.slider("Jumlah Makan Utama per Hari", 1.0, 4.0, 3.0, step=0.1)
        ch2o = st.slider("Konsumsi Air Minum per Hari (1: <1L, 3: >2L)", 1.0, 3.0, 2.0, step=0.1)
        faf = st.slider("Frekuensi Olahraga/Aktivitas Fisik (0: Tidak Pernah, 3: Rutin)", 0.0, 3.0, 1.0, step=0.1)
        tue = st.slider("Waktu Penggunaan Gadget per Hari (0: Rendah, 2: Tinggi)", 0.0, 2.0, 1.0, step=0.1)
        caec_ui = st.selectbox("Kebiasaan Ngemil di Antara Jam Makan", ["Kadang-kadang", "Sering", "Selalu", "Tidak Pernah"])
        calc_ui = st.selectbox("Konsumsi Alkohol", ["Tidak Pernah", "Kadang-kadang", "Sering", "Selalu"])
        mtrans_ui = st.selectbox("Transportasi Utama yang Digunakan", ["Transportasi Umum", "Mobil Pribadi", "Jalan Kaki", "Sepeda Motor", "Sepeda"])
    
    submit = st.form_submit_button("Analisis Risiko Obesitas 🔍")

if submit:
    # Mengumpulkan input dari form ke dalam satu dictionary
    inputs_ui = {
        'gender': gender_ui, 'age': age, 'height': height, 'weight': weight,
        'family_history': family_history_ui, 'favc': favc_ui, 'fcvc': fcvc, 'ncp': ncp,
        'caec': caec_ui, 'smoke': smoke_ui, 'ch2o': ch2o, 'scc': scc_ui, 'faf': faf,
        'tue': tue, 'calc': calc_ui, 'mtrans': mtrans_ui
    }
    
    # Panggil fungsi modular dari folder src/
    raw_input_df = preprocess_ui_input(inputs_ui)
    hasil_akhir = predict_obesity_risk(raw_input_df)
    
    st.markdown("---")
    st.subheader("📊 Hasil Analisis AI:")
    st.success(f"Berdasarkan indikator klinis, status Anda masuk ke dalam kategori: **{hasil_akhir}**")