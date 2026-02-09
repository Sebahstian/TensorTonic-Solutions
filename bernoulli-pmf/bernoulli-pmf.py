import numpy as np


def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    np_array = np.array(x)
    pmf = np.where(np_array == 1, (p ** 1) * (1 - p) ** (1 - 1), 1 - p)
    mean = float(p)
    var = float(p * (1 - p))
    
    return pmf, mean, var