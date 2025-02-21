from numpy import linspace
from main import get_sample_mean, get_mean

# Do this a number of times with different k and different p to show that the theoretical mean is right.
for ki in linspace(2, 6, 5, dtype=int):
    for pi in linspace(0.05, 1, 20):
        sample_mean = get_sample_mean(ki, pi)
        theoretical_mean = get_mean(ki, pi)
        print(f"k={ki:.0f}, p={pi:.2f}: sample_mean = {sample_mean:.4f} (with confidence interval [{sample_mean * 0.95:.4f}, {sample_mean * 1.05:.4f}]), expected value = {theoretical_mean:.4f}")