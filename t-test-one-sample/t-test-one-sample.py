import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    mean = np.mean(x)
    n = len(x)
    samp_std = np.std(x, ddof=1)
    t_stat = (mean - mu0) / (samp_std / np.sqrt(n))
    return t_stat