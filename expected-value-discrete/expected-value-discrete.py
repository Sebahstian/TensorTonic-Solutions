import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    close_sum = np.allclose(np.sum(p), 1.0)
    if not close_sum == 1.0:
        raise ValueError("Probabilities must sum to 1")
    else:
        np_array1 = np.array(x)
        np_array2 = np.array(p)
        expect_value = np.sum(np_array1 * np_array2)
        return expect_value
