# visualization.py — Rai perlu update jadi seperti ini

import numpy as np
import matplotlib.pyplot as plt
import os

def buat_visualisasi(x, y, y_pred, residuals, beta0, beta1, R2):  # ← wrap jadi fungsi

    os.makedirs("output", exist_ok=True)

    # Plot 1: Scatter + Garis Regresi
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color="steelblue", label="Data (xi, yi)", zorder=3)
    plt.plot(np.sort(x), beta0 + beta1 * np.sort(x), color="tomato", linewidth=2,
             label=f"Regresi: ŷ = {beta0:.4f} + {beta1:.4f}x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Scatter Plot & Garis Regresi")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/scatter_regression.png", dpi=150)
    plt.savefig("laporan/gambar/scatter_regression.png", dpi=150)  # ← copy ke laporan juga
    plt.show()

    # Plot 2: Residual Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(x, residuals, color="mediumpurple", zorder=3)
    plt.axhline(0, color="black", linewidth=1.2, linestyle="--")
    plt.xlabel("x")
    plt.ylabel("Residual (yi - ŷi)")
    plt.title("Residual Plot")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/residual_plot.png", dpi=150)
    plt.savefig("laporan/gambar/residual_plot.png", dpi=150)  # ← copy ke laporan juga
    plt.show()