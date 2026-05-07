import numpy as np

def scale_cols(data, weights):
    """Returns: np.ndarray of shape (m, n), each column scaled by corresponding weight"""

    arr = np.array(data, dtype=np.float64)
    arr2 = np.array(weights, dtype=np.float64)

    scale = arr * arr2

    return scale