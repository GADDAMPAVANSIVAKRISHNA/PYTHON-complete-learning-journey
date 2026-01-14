"""Indexing and slicing in numpy."""

import numpy as np


def slice_example():
    a = np.arange(12).reshape(3,4)
    return a[1:, 2:]


# Practice (5):
# 1) Use boolean masks to select elements.
# 2) Advanced indexing examples (fancy indexing).
# 3) Use views vs copies and show effects of modification.
# 4) Index using integer arrays to rearrange rows.
# 5) Use slice stepping and negative indices.

if __name__ == "__main__":
    print(slice_example())
    a = np.arange(12).reshape(3,4)
    mask = a%2==0
    print('evens', a[mask])
