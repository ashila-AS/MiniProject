# Mini Project — Least Squares Regression

Implementasi **Least Squares Regression** menggunakan Python untuk menentukan garis regresi terbaik dari sekumpulan data menggunakan pendekatan Persamaan Normal (*Normal Equation*).

**Mata Kuliah:** Aljabar Linear
**Program Studi:** D3 Teknik Informatika
**Institusi:** Politeknik Negeri Bandung

---

# Deskripsi Project

Project ini mengimplementasikan regresi linear sederhana menggunakan metode **Least Squares**.

Data dibangkitkan berdasarkan model:

[
y = \beta_0 + \beta_1x + \varepsilon
]

dengan parameter:

* β₀ = 2
* β₁ = 3
* ε ~ N(0, 0.5²)

Nilai x dibangkitkan secara seragam menggunakan:

```python
np.linspace(0, 10, 20)
```

Parameter regresi dihitung menggunakan Persamaan Normal:

[
\hat{\beta} = (A^T A)^{-1} A^T b
]

---

# Tujuan Project

* Memahami konsep Least Squares Regression.
* Mengimplementasikan operasi matriks menggunakan Python.
* Membentuk matriks desain regresi.
* Menghitung parameter regresi menggunakan Persamaan Normal.
* Mengevaluasi kualitas model menggunakan SSE, TSS, dan R².
* Membuat visualisasi hasil regresi dan residual.

---

# Anggota Kelompok

| No | Nama                 | Tanggung Jawab                        |
| -- | -------------------- | ------------------------------------- |
| 1  | Ashila Aulia Salwa   | Data Generation & Perhitungan Matriks |
| 2  | R. Neysa Rahma Velda | Evaluasi Model                        |
| 3  | Rainissa Azizah      | Visualisasi & Dokumentasi             |

---

# Struktur Project

```text
MiniProject/
│
├── data_generation.py
├── matrix_regression.py
├── evaluation.py
├── visualization.py
├── main.py
├── requirements.txt
├── README.md
│
├── output/
│   ├── matrices.txt
│   ├── hasil_evaluasi.txt
│   ├── scatter_regression.png
│   └── residual_plot.png
│
└── laporan/
    └── gambar/
        ├── scatter_regression.png
        └── residual_plot.png
```

---

# Library yang Digunakan

Project menggunakan library berikut:

* numpy
* matplotlib

Instalasi dependency:

```bash
pip install -r requirements.txt
```

atau

```bash
pip install numpy matplotlib
```

---

# Cara Menjalankan Program

Pastikan seluruh dependency telah terinstal.

Jalankan program menggunakan perintah:

```bash
python main.py
```

Program akan menjalankan tahapan berikut:

1. Membangkitan data regresi.
2. Membentuk matriks regresi.
3. Menghitung parameter β₀ dan β₁ menggunakan metode Least Squares.
4. Mengevaluasi model menggunakan SSE, TSS, dan R².
5. Menyimpan hasil perhitungan ke folder output.
6. Menampilkan visualisasi scatter plot dan garis regresi.
7. Menampilkan visualisasi residual plot.

---

# Cara Keluar dari Program

Program menggunakan Matplotlib untuk menampilkan grafik.

Visualisasi akan muncul **satu per satu**, sehingga pengguna perlu menutup jendela grafik yang sedang aktif agar program dapat melanjutkan ke tahap berikutnya.

### Langkah 1

Setelah grafik **Scatter Plot dan Garis Regresi** muncul:

* Tutup jendela grafik dengan menekan tombol **X**.
* Program akan melanjutkan ke visualisasi berikutnya.

### Langkah 2

Setelah grafik **Residual Plot** muncul:

* Tutup kembali jendela grafik dengan menekan tombol **X**.
* Program akan selesai dijalankan dan kembali ke terminal.

---

# Alur Eksekusi Program

```text
Jalankan main.py
        │
        ▼
Generate Data
        │
        ▼
Bentuk Matriks
        │
        ▼
Hitung Regresi
        │
        ▼
Evaluasi Model
        │
        ▼
Simpan Hasil ke Folder Output
        │
        ▼
Tampilkan Scatter Plot
        │
   (Tutup Window)
        ▼
Tampilkan Residual Plot
        │
   (Tutup Window)
        ▼
Program Selesai
```

---

# Contoh Output Terminal

```text
==================================================
   MINI PROJECT — LEAST SQUARES REGRESSION
==================================================

[1/3] Generate data & hitung regresi...
      β₀ = 1.8630
      β₁ = 3.0241
      Persamaan: y = 1.8630 + 3.0241x

[2/3] Evaluasi model...
      SSE = 3.4896
      TSS = 1688.1452
      R²  = 0.9979

[3/3] Membuat visualisasi...
      scatter_regression.png tersimpan
      residual_plot.png tersimpan

==================================================
   SEMUA SELESAI!
   Cek folder output/
==================================================
```

---

# File Output

Program menghasilkan beberapa file pada folder `output/`.

| File                   | Deskripsi                                             |
| ---------------------- | ----------------------------------------------------- |
| matrices.txt           | Matriks desain, matriks normal, dan parameter regresi |
| hasil_evaluasi.txt     | Nilai SSE, TSS, R², dan residual                      |
| scatter_regression.png | Grafik scatter plot dan garis regresi                 |
| residual_plot.png      | Grafik residual                                       |

---

# Hasil Regresi

Contoh hasil yang diperoleh:

```text
β₀ = 1.862958
β₁ = 3.024115
```

Persamaan regresi:

```text
y = 1.862958 + 3.024115x
```

---

# Hasil Evaluasi

```text
SSE = 3.4896
TSS = 1688.1452
R²  = 0.9979
```

Interpretasi:

Model memiliki nilai R² yang sangat mendekati 1, sehingga garis regresi mampu menjelaskan hampir seluruh variasi data yang diamati.

---

# Konsep Aljabar Linear yang Digunakan

* Matriks Desain (*Design Matrix*)
* Transpose Matriks
* Perkalian Matriks
* Invers Matriks
* Sistem Persamaan Linear
* Persamaan Normal (*Normal Equation*)
* Least Squares Regression
* Residual Analysis
* Sum of Squared Errors (SSE)
* Total Sum of Squares (TSS)
* Coefficient of Determination (R²)

---

# Visualisasi

### Scatter Plot dan Garis Regresi

Menampilkan titik data hasil pembangkitan serta garis regresi yang diperoleh dari metode Least Squares.

### Residual Plot

Menampilkan distribusi residual untuk membantu mengevaluasi kualitas model regresi.

---

# Catatan

Selama jendela visualisasi masih terbuka, program akan berhenti sementara (*blocking process*). Oleh karena itu, pengguna harus menutup jendela grafik yang aktif untuk melanjutkan proses program hingga selesai.

---

# Lisensi

Project ini dibuat untuk keperluan akademik pada mata kuliah Aljabar Linear Program Studi D3 Teknik Informatika Politeknik Negeri Bandung.