import numpy as np


def draw_bs_reps(data, func, size=1):
    """
    Performs bootstrap method to compute 95pc confidence interval of stat
    value.
    inputs are (data, func, size=1)
    func e.g. np.mean or np.std
    returns confidence interval.
    """
    n = len(data)
    reps = np.empty(size)
    for i in range(size):
        bs_sample = np.random.choice(data, replace=True, size=len(data))
        reps[i] = func(bs_sample)

    return np.percentile(reps, (2.5, 97.5))
