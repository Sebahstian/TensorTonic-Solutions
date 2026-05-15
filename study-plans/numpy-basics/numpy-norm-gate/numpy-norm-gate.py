import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""

    Z = np.dot(X, W)

    norms = np.linalg.norm(Z, axis=1)

    gate = (norms >= threshold).astype(np.float64)[:, np.newaxis]
    
    return Z * gate