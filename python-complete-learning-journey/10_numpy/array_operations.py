"""Array operations in numpy."""

import numpy as np


def dot_product(a, b):
    return np.dot(a, b)


# Practice (5):
# 1) Implement elementwise operations and broadcasting examples.
# 2) Reshape arrays without copying.
# 3) Compute matrix multiplication vs elementwise product.
# 4) Use einsum for custom tensor operations.
# 5) Benchmark different approaches for dot vs manual python loops.

if __name__ == "__main__":
    print(dot_product([1,2],[3,4]))
    a = np.arange(6).reshape(2,3)
    b = np.arange(3)
    print('broadcast add', a + b)
