import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    a = np.sort(x)
    b = np.percentile(a, q, method='linear')
    return b