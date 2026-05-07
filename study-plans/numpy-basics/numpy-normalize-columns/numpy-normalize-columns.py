import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""

    arr = np.array(data, dtype=np.float64)

    norm = (arr - arr.mean(axis=0)) / arr.std(axis=0)

    return norm