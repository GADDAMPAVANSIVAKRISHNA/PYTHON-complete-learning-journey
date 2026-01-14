"""Common numpy functions and practical exercises."""

import numpy as np


def mean_std(arr):
    a = np.array(arr)
    return a.mean(), a.std()


# Practice (5):
# 1) Compute running average using convolution.
# 2) Use numpy vectorize vs pure python.
# 3) Implement moving window std efficiently.
# 4) Use numpy builtin functions for common statistics.
# 5) Use masked arrays to exclude invalid values.

if __name__ == "__main__":
    print(mean_std([1,2,3,4,5]))
