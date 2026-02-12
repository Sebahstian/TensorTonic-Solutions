import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    array = np.array(C) # Creating 2D Arrays
    sum_row = np.sum(array, axis=1) # Sum of Rows
    sum_col = np.sum(array, axis=0) # Sum of Columns
    expected = np.outer(sum_row, sum_col) / np.sum(C) # Expected Frequencies
    chi_square = np.sum(((C - expected) ** 2) / expected) # Chi-Square Test
    return chi_square, expected