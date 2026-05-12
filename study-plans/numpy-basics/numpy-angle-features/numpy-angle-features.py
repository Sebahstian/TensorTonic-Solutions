import numpy as np

def angle_features(angles):
    """Returns: np.ndarray of shape (3, n), rows are sin, cos, tan"""

    sine = np.sin(angles)
    cosine = np.cos(angles)
    tangent = np.tan(angles)

    arr = np.array([sine, cosine, tangent], dtype=np.float64)

    return arr
    