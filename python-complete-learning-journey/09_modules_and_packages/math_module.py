"""Examples using the math module and practice."""

import math


def circle_area(r):
    return math.pi * r * r


# Practice (5):
# 1) Use math.isclose for float comparisons.
# 2) Demonstrate math.comb and math.perm.
# 3) Use math.gcd and math.lcm for integer operations.
# 4) Compute combinations/permutations for given n and k.
# 5) Demonstrate math.trunc, floor, ceil differences.

if __name__ == "__main__":
    print(circle_area(2))
    print('comb(5,2)=', math.comb(5,2))
