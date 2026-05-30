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
        y = beta0 + beta1*x + epsilon

    dengan:
        epsilon ~ N(0, noise_std^2)
    """

    rng = np.random.default_rng(seed)

    x = rng.uniform(x_min, x_max, n_samples)
    epsilon = rng.normal(0, noise_std, n_samples)

    y = beta0 + beta1 * x + epsilon

    return x, y


if __name__ == "__main__":
    x, y = generate_data()

    print("x:")
    print(x)

    print("\ny:")
    print(y)