import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    x = np.asarray(X, dtype=float)
    mu = x.mean(axis=axis, keepdims=True)
    sigma = x.std(axis=axis, keepdims=True)
    return np.where(sigma <= eps, 0.0, (x - mu) / sigma)