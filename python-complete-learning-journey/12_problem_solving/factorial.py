"""Factorial examples and practice."""


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('n must be non-negative')
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


# Practice (5):
# 1) Compute factorial of large numbers using iterative and recursive methods.
# 2) Use `math.factorial` and compare performance.
# 3) Compute trailing zeros of n! without computing factorial directly.
# 4) Use memoization to speed repeated factorial computations.
# 5) Compute factorial modulo m for combinatorics use-cases.

# Sample: trailing zero function
def trailing_zeros(n):
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count

if __name__ == "__main__":
    print(factorial(5))
    print('trailing zeros 100! =', trailing_zeros(100))
