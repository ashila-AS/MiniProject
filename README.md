# Mini Project — Least Squares Regression

Implementasi metode **Least Squares Regression** menggunakan Python untuk mencari garis regresi terbaik berdasarkan data yang dibangkitkan secara acak.

**Mata Kuliah:** Aljabar Linear
**Program Studi:** D3 Teknik Informatika
**Institusi:** Politeknik Negeri Bandung

---

## Deskripsi Project

Project ini bertujuan untuk menerapkan konsep **Regresi Linear Sederhana** dan **Metode Kuadrat Terkecil (Least Squares Method)** menggunakan pendekatan matriks.

Sebanyak **20 titik data** dibangkitkan dari model:

[
y = 2 + 3x + \varepsilon
]

dengan:

* (x) : variabel independen
* (y) : variabel dependen
* (\varepsilon \sim N(0, 0.5^2)) : noise acak berdistribusi normal

Parameter regresi dihitung menggunakan persamaan normal:

[
\hat{\beta} = (A^T A)^{-1} A^T b
]

Hasil model kemudian dievaluasi menggunakan:

* Residual
* SSE (Sum of Squared Errors)
* TSS (Total Sum of Squares)
* Coefficient of Determination ((R^2))

---

## Anggota Kelompok

| No | Nama                | Tanggung Jawab                          |
| -- | ------------------- | --------------------------------------- |
| 1  | Ashila Aulia Salwa  | Data Generation & Perhitungan Matriks   |
| 2  | R. Neysa Rahma Velda| Evaluasi Model (Residual, SSE, TSS, R²) |
| 3  | Rainissa Azizah     | Visualisasi Data & Penyusunan Laporan   |

---

## Struktur Project

```text
mini-project-least-squares/
│
├── data_generation.py
├── matrix_regression.py
├── evaluation.py
├── visualization.py
├── main.py
│
├── output/
│   ├── scatter_regression.png
│   ├── residual_plot.png
│   └── result.txt
│
├── laporan/
│
├── requirements.txt
└── README.md
```

---

## Instalasi

Clone repository:

```bash
git clone <repository-url>
cd mini-project-least-squares
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

## Menjalankan Program

Jalankan program utama:

```bash
python main.py
```

---

## Output

Program akan menghasilkan:

### 1. Scatter Plot & Garis Regresi

Visualisasi data hasil pembangkitan beserta garis regresi terbaik.

```text
output/scatter_regression.png
```

### 2. Residual Plot

Visualisasi distribusi residual terhadap nilai prediksi.

```text
output/residual_plot.png
```

### 3. Hasil Evaluasi

Berisi parameter regresi dan metrik evaluasi model.

```text
output/result.txt
```

Contoh:

```text
β0 = 2.08
β1 = 2.94

SSE = 4.13
TSS = 152.78
R²  = 0.973
```

---

## Konsep yang Digunakan

* Sistem Persamaan Linear
* Operasi Matriks
* Least Squares Regression
* Residual Analysis
* Sum of Squared Errors (SSE)
* Total Sum of Squares (TSS)
* Coefficient of Determination (R²)
* Data Visualization

---

## Lisensi

Project ini dibuat untuk keperluan akademik pada mata kuliah Aljabar Linear.
