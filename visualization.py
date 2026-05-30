import numpy as np
import matplotlib.pyplot as plt
import os

from data_generation import generate_data
from matrix_regression import least_squares_regression
from evaluation import evaluasi_model

# ── Ambil data & hasil regresi ──
x, y = generate_data()
result = least_squares_regression(x, y)
beta0 = result["beta0"]
beta1 = result["beta1"]
y_pred, residuals, SSE, TSS, R2 = evaluasi_model(x, y, beta0, beta1)

# Bikin folder output otomatis
os.makedirs("output", exist_ok=True)

# ── Plot 1: Scatter + Garis Regresi ──
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
plt.show()
print("Scatter plot tersimpan.")

# ── Plot 2: Residual Plot ──
plt.figure(figsize=(8, 5))
plt.scatter(x, residuals, color="mediumpurple", zorder=3)
plt.axhline(0, color="black", linewidth=1.2, linestyle="--")
plt.xlabel("x")
plt.ylabel("Residual (yi - ŷi)")
plt.title("Residual Plot")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/residual_plot.png", dpi=150)
plt.show()
print("Residual plot tersimpan.")