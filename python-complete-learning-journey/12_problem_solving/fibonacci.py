"""Fibonacci implementations and exercises."""


def fib_iter(n):
    a, b = 0, 1
    res = []
    for _ in range(n):
        res.append(a)
        a, b = b, a + b
    return res


# Practice (5):
# 1) Implement fast doubling method for Fibonacci.
# 2) Check if a number is Fibonacci (via perfect square test).
# 3) Implement Fibonacci with memoization and tabulation.
# 4) Compute nth Fibonacci modulo m efficiently.
# 5) Find the index of a Fibonacci number if it exists.

# Sample solution (memoization):
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    print(fib_iter(10))
    print('memo 10th=', fib_memo(10))
