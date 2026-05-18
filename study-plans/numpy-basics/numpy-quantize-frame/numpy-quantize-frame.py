import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""

    arr = np.array(data, dtype=np.float64)

    f_round = np.round(arr, decimals)
    f_floor = np.floor(arr)
    f_ceil = np.ceil(arr)

    pad_round = np.pad(f_round, pad_width)
    pad_floor = np.pad(f_floor, pad_width)
    pad_ceil = np.pad(f_ceil, pad_width)
    
    return np.stack([pad_round, pad_floor, pad_ceil])