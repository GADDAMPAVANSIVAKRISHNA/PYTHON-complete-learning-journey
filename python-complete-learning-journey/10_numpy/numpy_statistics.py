"""NumPy statistical helpers and exercises"""

import numpy as np


def percentile(arr, p):
    return np.percentile(np.array(arr), p)


# Practice (5):
# 1) Compute trimmed mean.
# 2) Use numpy to compute correlation coefficient.
# 3) Implement winsorized mean.
# 4) Compute z-scores and detect outliers.
# 5) Use quantiles to bucket continuous data.

if __name__ == "__main__":
    print(percentile([1,2,3,4,5], 50))
    a = np.array([1,2,3,4,100])
    print('z-scores', (a - a.mean())/a.std())
