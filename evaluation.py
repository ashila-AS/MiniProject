# evaluation.py

import numpy as np

def evaluasi_model(x, y, beta0, beta1):
    
    # Langkah 1: Prediksi
    y_pred = beta0 + beta1 * x
    
    # Langkah 2: Residual
    r = y - y_pred
    
    # Langkah 3: SSE
    SSE = np.sum(r**2)
    
    # Langkah 4: TSS
    y_mean = np.mean(y)
    TSS = np.sum((y - y_mean)**2)
    
    # Langkah 5: R²
    R2 = 1 - SSE / TSS
    
    # Langkah 6: Interpretasi
    if R2 >= 0.95:
        interpretasi = f"Model sangat baik — garis regresi menjelaskan {R2*100:.2f}% variasi data."
    elif R2 >= 0.80:
        interpretasi = f"Model cukup baik — garis regresi menjelaskan {R2*100:.2f}% variasi data."
    else:
        interpretasi = f"Model kurang fit — hanya menjelaskan {R2*100:.2f}% variasi data."
    
    # Simpan hasil ke file teks (untuk laporan)
    with open("output/hasil_evaluasi.txt", "w") as f:
        f.write("=" * 45 + "\n")
        f.write("         HASIL EVALUASI MODEL\n")
        f.write("=" * 45 + "\n")
        f.write(f"  β₀ (intercept) = {beta0:.4f}\n")
        f.write(f"  β₁ (slope)     = {beta1:.4f}\n")
        f.write(f"  Persamaan      : y = {beta0:.4f} + {beta1:.4f}x\n")
        f.write("-" * 45 + "\n")
        f.write(f"  SSE            = {SSE:.4f}\n")
        f.write(f"  TSS            = {TSS:.4f}\n")
        f.write(f"  R²             = {R2:.4f}\n")
        f.write("-" * 45 + "\n")
        f.write(f"  INTERPRETASI:\n  {interpretasi}\n")
        f.write("=" * 45 + "\n\n")
        f.write("  TABEL RESIDUAL:\n")
        f.write(f"  {'i':>3} | {'xᵢ':>6} | {'yᵢ':>6} | {'ŷᵢ':>6} | {'rᵢ':>7} | {'rᵢ²':>8}\n")
        f.write("  " + "-" * 48 + "\n")
        for i in range(len(x)):
            f.write(f"  {i+1:>3} | {x[i]:>6.2f} | {y[i]:>6.2f} | "
                    f"{y_pred[i]:>6.2f} | {r[i]:>7.4f} | {r[i]**2:>8.4f}\n")
        f.write("  " + "-" * 48 + "\n")
        f.write(f"  {'TOTAL SSE':>38} | {SSE:>8.4f}\n")
    
    # Print ke terminal juga
    print("=" * 45)
    print("         HASIL EVALUASI MODEL")
    print("=" * 45)
    print(f"  β₀ = {beta0:.4f}")
    print(f"  β₁ = {beta1:.4f}")
    print(f"  y  = {beta0:.4f} + {beta1:.4f}x")
    print("-" * 45)
    print(f"  SSE = {SSE:.4f}")
    print(f"  TSS = {TSS:.4f}")
    print(f"  R²  = {R2:.4f}")
    print("-" * 45)
    print(f"  {interpretasi}")
    print("=" * 45)
    
    return y_pred, r, SSE, TSS, R2