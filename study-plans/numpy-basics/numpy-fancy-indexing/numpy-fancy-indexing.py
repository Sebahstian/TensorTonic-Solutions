import numpy as np

def select_by_index(arr, indices, axis):
    """
    Returns: 2D ndarray of float64
    """
    array = np.array(arr, dtype=np.float64)

    if axis == 0:
        return array[indices, :]
    elif axis == 1:
        return array[:, indices]