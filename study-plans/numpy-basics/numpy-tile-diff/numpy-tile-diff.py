import numpy as np

def tile_diff(data, reps):
    """Returns: np.ndarray of shape (2, m*reps, n), stacked tiled array and padded differences"""

    arr = np.array(data, dtype=np.float64)

    tiled = np.tile(arr, (reps, 1))

    padded = np.pad(tiled, ((0, 1), (0, 0)), mode='edge')

    diffs = np.diff(padded, axis=0)
    
    return np.stack([tiled, diffs])