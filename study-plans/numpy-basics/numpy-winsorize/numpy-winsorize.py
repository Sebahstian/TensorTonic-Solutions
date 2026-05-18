import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""

    arr = np.array(data, dtype=np.float64)

    lo_res = np.percentile(arr, lo_q, axis=0)
    hi_res = np.percentile(arr, hi_q, axis=0)
    
    clipped = np.clip(arr, lo_res, hi_res)

    low_clipped = np.where(arr < lo_res, 1, 0)
    
    high_clipped = np.where(arr > hi_res, 1, 0)

    return np.stack([clipped, low_clipped, high_clipped])