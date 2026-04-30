import numpy as np

def create_sequence(start, stop, param, kind):
    """
    Returns: 1D ndarray of float64 values
    """
    if kind == 'arange':
        return np.array(np.arange(start, stop, param), dtype=np.float64)
    elif kind == 'linspace':
        return np.array(np.linspace(start, stop, param), dtype=np.float64)
