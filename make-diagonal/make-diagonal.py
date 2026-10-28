import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    n = len(v)
    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = v[i]

    return A