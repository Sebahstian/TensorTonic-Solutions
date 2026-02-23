import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    array = np.array(x) # turning data into an array
    n = len(x) # Length of the sample
    if rng is None:
      rng = np.random

    boot = []
    for _ in range(n_bootstrap): # Bootstraping using the loop 1000
      indices = rng.integers(0, n, n) \
      if hasattr(rng, 'integers') else \
      rng.randint((0, n, n))
      sample = array[indices]
      boot.append(np.mean(sample))
    
    boot_means = np.array(boot)
  
    a = 1 - ci
    low = a / 2
    high = (1 - low)
    upper = np.quantile(boot_means, high) # Confidence Intervals of 95%
    lower = np.quantile(boot_means, low) # Confidence Intervals of 5%

    return boot_means, lower, upper