import numpy as np


def generate_data(
    n_samples=20,
    x_min=0.0,
    x_max=10.0,
    beta0=2.0,
    beta1=3.0,
    noise_std=0.5,
    seed=42
):
    """
    Generate data dari model:
        y = beta0 + beta1 * x + epsilon

    dengan:
        x dibangkitkan menggunakan np.linspace()
        epsilon ~ N(0, noise_std^2)
    """

    rng = np.random.default_rng(seed)

    x = np.linspace(x_min, x_max, n_samples)

    epsilon = rng.normal(0, noise_std, n_samples)

    y = beta0 + beta1 * x + epsilon

    return x, y


if __name__ == "__main__":
    x, y = generate_data()

    print("Data x:")
    print(x)

    print("\nData y:")
    print(y)

    print("\nTabel Data")
    print("-" * 25)
    print(f"{'No':<4}{'x':<10}{'y':<10}")

    for i in range(len(x)):
        print(f"{i+1:<4}{x[i]:<10.4f}{y[i]:<10.4f}")