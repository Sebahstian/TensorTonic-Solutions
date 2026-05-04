import numpy as np

def outer_sum(a, b):
    """Returns: np.ndarray of shape (m, n), outer sum where out[i,j] = a[i] + b[j]"""

    arr = np.array(a, dtype=np.float64)
    arr2 = np.array(b, dtype=np.float64)
    
    outer = arr[:, None] + arr2[None, :]

    return outer