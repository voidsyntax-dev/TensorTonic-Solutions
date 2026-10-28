import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    X = np.array(X)
    h, l = X.max(axis = axis, keepdims = True), X.min(axis = axis, keepdims = True)
    return np.where(h-l <= eps, 0, (X-l)/(h-l))