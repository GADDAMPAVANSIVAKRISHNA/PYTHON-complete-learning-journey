"""Numpy basics: array creation and practice problems."""

import numpy as np


def create_array(n):
    return np.arange(n)


# Practice (5):
# 1) Create a 2D grid and compute mean across axes.
# 2) Use boolean indexing to filter arrays.
# 3) Reshape and view vs copy behavior.
# 4) Vectorize a python function using numpy.vectorize.
# 5) Use broadcasting to add a vector to matrix rows.

if __name__ == "__main__":
    print(create_array(5))
    a = np.arange(6).reshape(2,3)
    print('mean axis0', a.mean(axis=0))
