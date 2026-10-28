import numpy as np

def log_transform(values: list) -> list:
    return np.log(np.array(values) + 1)    