"""
A function to complete theoretical fold change.
"""

import numpy as np


# Solves the top part of fraction in function.
def top_fold_change(RK, c, KdA):
    return RK * (1 + c / KdA)**2

def bottom_fold_change(c, KdA, KdI, Kswitch):
    return (1 + c / KdA)**2 + Kswitch * (1 + c / KdI)**2


# Complete function.
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch = 5.8):
    top = top_fold_change(RK, c, KdA)
    bot = bottom_fold_change(c, KdA, KdI, Kswitch)
    th_fold_change = (1 + top / bot)**-1
    return th_fold_change
