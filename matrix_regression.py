import numpy as np
from pathlib import Path

def build_design_matrix(x):
    """
    Membentuk matriks desain:
        A = [1  x]
    ukuran:
        (n x 2)
    """
    x = np.asarray(x, dtype=float)
    A = np.column_stack(
        (
            np.ones(len(x)),
            x
        )
    )
    return A

def least_squares_regression(x, y):
    """
    Menyelesaikan Least Squares menggunakan:
        (A^T A)x = A^T b
    Return:
        Dictionary berisi komponen matriks dan hasil regresi
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if len(x) != len(y):
        raise ValueError("Jumlah data x dan y harus sama.")

    A = build_design_matrix(x)
    b = y.reshape(-1, 1)

    AT = A.T
    ATA = AT @ A
    ATb = AT @ b

    beta = np.linalg.solve(ATA, ATb)

    beta0 = float(beta[0, 0])
    beta1 = float(beta[1, 0])

    y_pred = beta0 + beta1 * x

    return {
        "A": A,
        "b": b,
        "AT": AT,
        "ATA": ATA,
        "ATb": ATb,
        "beta0": beta0,
        "beta1": beta1,
        "y_pred": y_pred
    }

def save_matrix_results(result, filename="output/matrices.txt"):
    """
    Menyimpan hasil matriks ke file txt dengan format yang rapi.
    """
    output_path = Path(filename)  
    output_path.parent.mkdir(parents=True, exist_ok=True)  

    opt = {"max_line_width": 100, "precision": 4, "suppress_small": True}

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("=== MATRIKS A ===\n")
        file.write(f"{np.array2string(result['A'], **opt)}\n\n")

        file.write("=== VEKTOR b ===\n")
        file.write(f"{np.array2string(result['b'], **opt)}\n\n")

        file.write("=== MATRIKS A^T ===\n")
        file.write(f"{np.array2string(result['AT'], **opt)}\n\n")

        file.write("=== MATRIKS A^T A ===\n")
        file.write(f"{np.array2string(result['ATA'], **opt)}\n\n")

        file.write("=== VEKTOR A^T b ===\n")
        file.write(f"{np.array2string(result['ATb'], **opt)}\n\n")

        file.write(f"beta0 = {result['beta0']:.6f}\n")
        file.write(f"beta1 = {result['beta1']:.6f}\n")
        file.write("\nPersamaan Regresi:\n")
        file.write(f"y = {result['beta0']:.6f} + {result['beta1']:.6f}x\n")

if __name__ == "__main__":
    try:
        from data_generation import generate_data
        
        x, y = generate_data()
        result = least_squares_regression(x, y)
        save_matrix_results(result)

        print(f"beta0 = {result['beta0']:.6f}")
        print(f"beta1 = {result['beta1']:.6f}")
        print("\nFile berhasil disimpan ke: output/matrices.txt")
        
    except ImportError:
        print("Error: Pastikan file 'data_generation.py' berada di folder yang sama dengan script ini!")