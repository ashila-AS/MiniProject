# Mini Project — Least Squares Regression
**Mata Kuliah:** Aljabar Linear  
**Kelas:** D3 Teknik Informatika — Politeknik Negeri Bandung  

## Anggota Kelompok
| Orang | Nama | Bagian |
|-------|------|--------|
| 1 | Ashila | Perhitungan Matriks |
| 2 | Neztt | Evaluasi Model |
| 3 | Rai | Visualisasi & Laporan |

---

## Cara Menjalankan

### 1. Install library yang dibutuhkan
pip install -r requirements.txt

### 2. Jalankan program
python main.py

### 3. Cek hasil output
output/
├── scatter_regression.png  ← grafik data + garis regresi
├── residual_plot.png        ← grafik residual
└── result.txt               ← hasil evaluasi (SSE, TSS, R²)

---

## Struktur File
mini-project-least-squares/
│
├── data_generation.py    → (Ashila) generate data acak
├── matrix_regression.py  → (Ashila) perhitungan matriks & regresi
├── evaluation.py         → (Neztt) SSE, TSS, R², interpretasi
├── visualization.py      → (Rai) scatter plot & residual plot
├── main.py               → gabungkan semua modul
│
├── output/               → hasil output otomatis dibuat
├── laporan/              → file laporan Word
├── requirements.txt      → daftar library
└── README.md             → panduan ini

---

## Deskripsi Singkat
Project ini menerapkan **Metode Kuadrat Terkecil (Least Squares)**  
untuk mencari garis regresi terbaik dari 20 titik data acak  
yang dibangkitkan dari model:

> **y = 2 + 3x + ε**, dengan ε ~ N(0, 0.5²)

Perhitungan dilakukan secara **manual menggunakan operasi matriks**:

> **β̂ = (AᵀA)⁻¹ Aᵀb**