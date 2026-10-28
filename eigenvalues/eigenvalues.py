import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    return np.sort(np.linalg.eigvals(matrix))