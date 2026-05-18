import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""

    arr = np.array(a, dtype=np.float64)

    arr2 = np.array(b, dtype=np.float64)

    conc = np.concatenate([arr, arr2], axis=0)

    a_corr = np.corrcoef(arr, rowvar=False)
    b_corr = np.corrcoef(arr2, rowvar=False)
    conc_corr = np.corrcoef(conc, rowvar=False)

    return np.stack([a_corr, b_corr, conc_corr])