import numpy as np
from collections import Counter
# List examples
a = [1,2,2,3,3]

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)
    # Calculating the mode
    counts = Counter(x)
    max_counts = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_counts]
    mode = float(min(modes))
    
    return mean, median, mode

