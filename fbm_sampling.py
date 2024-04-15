import scipy
from scipy.fft import hfft, ihfft, rfft
import numpy as np


def time_augmented_fbm(H, T, time_steps, samples):
    X = np.zeros((samples, time_steps + 1, 2))
    X[:, :, 0] = np.linspace(0, T, time_steps + 1)
    X[:, :, 1] = simulate_fbm(H=H, n=time_steps, delta=T / time_steps, m=samples)
    return X


def stationary_gaussian(c, n, m):
    gam = np.concatenate([c, c[1:-1][::-1]])
    lam = np.sqrt(rfft(gam))
    return hfft(lam * ihfft(np.random.randn(m, len(gam))))[:, :n]


def simulate_fbm(H, n, delta, m):
    cov = lambda k: 0.5 * (np.abs(k + 1) ** (2 * H) + np.abs(k - 1) ** (2 * H)) \
                    - np.abs(k) ** (2 * H)
    X = np.zeros((m, n + 1))
    X[:, 1:] = stationary_gaussian(cov(np.arange(n)), n, m)
    return delta ** H * np.cumsum(X, axis=1, out=X)
