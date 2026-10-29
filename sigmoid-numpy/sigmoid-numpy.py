import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    x = np.array(x)
    x = 1 / (1 + np.exp(-x))
    if x.ndim == 0:
        return float(x)
    else:
        return x
        