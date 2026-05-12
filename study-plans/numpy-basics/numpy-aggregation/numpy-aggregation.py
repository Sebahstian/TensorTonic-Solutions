import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    

    arr = np.array(data, dtype=np.float64)
    mean = np.mean(arr, axis=axis)
    std = np.std(arr, axis=axis)
    min = np.min(arr, axis=axis)
    max = np.max(arr, axis=axis)

    return np.stack([mean, std, min, max])