import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    np_array = np.array(k)
    pmf = ((1 - p)**(np_array - 1))*p
    mean = float(1 / p)
    return pmf, mean