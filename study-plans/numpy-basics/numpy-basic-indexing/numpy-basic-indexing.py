import numpy as np

def extract_subarray(arr, row_start, row_stop, col_start, col_stop):
    """
    Returns: 2D ndarray of float64
    """
    array = np.array(arr, dtype=np.float64)

    subarray = array[row_start:row_stop, col_start:col_stop]

    return subarray
