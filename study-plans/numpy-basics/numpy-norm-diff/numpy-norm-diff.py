import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""

    a_clipped = np.clip(a, lo, hi)
    b_clipped = np.clip(b, lo, hi)

    a_rescale = (a_clipped - lo) / (hi - lo)
    b_rescale = (b_clipped - lo) / (hi - lo)
    

    diff = np.abs(a_rescale - b_rescale).astype(np.float64)
    
    return diff