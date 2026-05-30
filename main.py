# main.py
# Menggabungkan seluruh modul

import os
from data_generation import generate_data
from matrix_regression import least_squares_regression, save_matrix_results
from evaluation import evaluasi_model
from visualization import buat_visualisasi

# Buat folder output
os.makedirs("output", exist_ok=True)
os.makedirs("laporan/gambar", exist_ok=True)

print("=" * 50)
print("   MINI PROJECT — LEAST SQUARES REGRESSION")
print("   Aljabar Linear — D3 Teknik Informatika")
print("=" * 50)

# ── STEP 1 & 2 — Ashila ──
print("\n[1/3] Generate data & hitung regresi...")
x, y = generate_data()
result = least_squares_regression(x, y)
save_matrix_results(result)
beta0 = result["beta0"]
beta1 = result["beta1"]
print(f"      β₀ = {beta0:.4f}")
print(f"      β₁ = {beta1:.4f}")
print(f"      Persamaan: y = {beta0:.4f} + {beta1:.4f}x")

# ── STEP 3 — Neysa ──
print("\n[2/3] Evaluasi model...")
y_pred, r, SSE, TSS, R2 = evaluasi_model(x, y, beta0, beta1)
print(f"      SSE = {SSE:.4f}")
print(f"      TSS = {TSS:.4f}")
print(f"      R²  = {R2:.4f}")

# ── STEP 4 — Rainissa ──
print("\n[3/3] Membuat visualisasi...")
buat_visualisasi(x, y, y_pred, r, beta0, beta1, R2)
print(f"      scatter_regression.png tersimpan")
print(f"      residual_plot.png tersimpan")

print("\n" + "=" * 50)
print("   SEMUA SELESAI! Cek folder output/")
print("=" * 50)