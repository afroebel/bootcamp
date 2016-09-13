# Empirical distribution function ecdf

import numpy as np

def ecdf(data):
    """
    Compute x, y values for empirical distribution function.
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y
