# Kamus Data - Prediksi Tingkat Obesitas

Dokumen ini menjelaskan seluruh variabel (fitur) beserta tipe data dan nilai unik yang digunakan di dalam dataset klasifikasi tingkat obesitas.

## 1. Fitur Demografi & Fisik
* **Gender** (Kategorikal)
  * Keterangan: Jenis kelamin responden.
  * Nilai: *Female* (Perempuan), *Male* (Laki-laki).
* **Age** (Numerik)
  * Keterangan: Umur responden dalam satuan tahun (Rentang data: 14 s.d. 61 tahun).
* **Height** (Numerik)
  * Keterangan: Tinggi badan responden dalam satuan meter.
* **Weight** (Numerik)
  * Keterangan: Berat badan responden dalam satuan kilogram.

## 2. Fitur Riwayat & Kebiasaan Makan
* **family_history_with_overweight** (Kategorikal/Kuesioner)
  * Keterangan: Apakah ada anggota keluarga responden yang memiliki riwayat kelebihan berat badan (obesitas).
  * Nilai: *yes* (Ya), *no* (Tidak).
* **FAVC** (Kategorikal/Kuesioner)
  * Keterangan: Apakah responden sering mengonsumsi makanan tinggi kalori (seperti makanan cepat saji / *junk food*).
  * Nilai: *yes* (Ya), *no* (Tidak).
* **FCVC** (Numerik/Skala)
  * Keterangan: Frekuensi konsumsi sayuran dalam makanan utama sehari-hari.
  * Nilai: Skala desimal antara 1 (Jarang) sampai 3 (Selalu).
* **NCP** (Numerik/Skala)
  * Keterangan: Jumlah frekuensi makan utama responden dalam sehari.
  * Nilai: Skala desimal antara 1 sampai 4 kali makan harian.
* **CAEC** (Kategorikal)
  * Keterangan: Kebiasaan mengonsumsi makanan kecil (ngemil) di antara jam-jam makan utama.
  * Nilai: *no* (Tidak pernah), *Sometimes* (Kadang-kadang), *Frequently* (Sering), *Always* (Selalu).

## 3. Fitur Gaya Hidup & Kebiasaan Fisik
* **SMOKE** (Kategorikal/Kuesioner)
  * Keterangan: Apakah responden memiliki kebiasaan merokok.
  * Nilai: *yes* (Ya), *no* (Tidak).
* **CH2O** (Numerik/Skala)
  * Keterangan: Jumlah konsumsi air minum harian responden.
  * Nilai: Skala desimal antara 1 (Kurang dari 1 Liter) sampai 3 (Lebih dari 2 Liter).
* **SCC** (Kategorikal/Kuesioner)
  * Keterangan: Apakah responden rutin memonitor atau menghitung jumlah kalori makanan yang dikonsumsi harian.
  * Nilai: *yes* (Ya), *no* (Tidak).
* **FAF** (Numerik/Skala)
  * Keterangan: Frekuensi melakukan aktivitas fisik atau olahraga dalam seminggu.
  * Nilai: Skala desimal antara 0 (Tidak pernah) sampai 3 (Sangat rutin).
* **TUE** (Numerik/Skala)
  * Keterangan: Waktu yang dihabiskan responden di depan layar perangkat elektronik atau gadget (*Time Using Technology Devices*) per hari.
  * Nilai: Skala desimal antara 0 (Rendah) sampai 2 (Tinggi).
* **CALC** (Kategorikal)
  * Keterangan: Frekuensi konsumsi minuman beralkohol.
  * Nilai: *no* (Tidak pernah), *Sometimes* (Kadang-kadang), *Frequently* (Sering), *Always* (Selalu).
* **MTRANS** (Kategorikal)
  * Keterangan: Jenis moda transportasi utama yang digunakan responden sehari-hari untuk bepergian.
  * Nilai: *Automobile* (Mobil pribadi), *Bike* (Sepeda), *Motorbike* (Sepeda Motor), *Public_Transportation* (Transportasi Umum), *Walking* (Jalan Kaki).

## 4. Variabel Target (Output Klasifikasi)
* **NObeyesdad** (Kategorikal)
  * Keterangan: Tingkat kategori berat badan/obesitas responden berdasarkan kalkulasi BMI (*Body Mass Index*).
  * Nilai (7 Kelas):
    * *Insufficient Weight* (Kekurangan Berat Badan)
    * *Normal Weight* (Berat Badan Normal)
    * *Overweight Level I* (Kelebihan Berat Badan Tingkat I)
    * *Overweight Level II* (Kelebihan Berat Badan Tingkat II)
    * *Obesity Type I* (Obesitas Tipe I)
    * *Obesity Type II* (Obesitas Tipe II)
    * *Obesity Type III* (Obesitas Ekstrem Tipe III)