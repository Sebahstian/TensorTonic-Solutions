import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
  # Using a log function for factorial computation
    log = (k * np.log(lam)) - lam - np.log(np.arange(1, k + 1)).sum()
  # Using a function to calculate exponential
    pmf = np.exp(log)
  # A for loop to sum up the cdf
    cdf = 0
    for i in range(k + 1):
      log2 = (i * np.log(lam)) - lam - np.log(np.arange(1, i + 1)).sum()
      pmf2 = np.exp(log2)
      cdf += pmf2
    return pmf, cdf