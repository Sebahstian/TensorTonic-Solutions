import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""

    arr = np.array(data, dtype=np.float64)

    max = arr.max(axis=1)
    max2 = np.argmax(arr, axis=1)
    min = arr.min(axis=1)
    min2 = np.argmin(arr, axis=1)

  
    
    return np.stack([max, max2, min, min2])
