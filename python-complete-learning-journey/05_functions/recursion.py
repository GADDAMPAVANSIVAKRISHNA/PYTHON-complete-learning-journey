"""Recursion examples and practice problems."""


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


# Practice (5):
# 1) Implement Fibonacci recursively and iteratively.
# 2) Use recursion to traverse nested lists.
# 3) Write recursive solutions for binary tree traversal (simple lists).
# 4) Convert recursion into tail recursion (conceptually) and iterative form.
# 5) Detect and avoid infinite recursion (add depth guard).

# Sample solution for 2 (nested list sum):
def nested_sum(lst):
    total = 0
    for x in lst:
        if isinstance(x, list):
            total += nested_sum(x)
        else:
            total += x
    return total

if __name__ == "__main__":
    print(factorial(5))
    print(nested_sum([1,[2,3],[4,[5]]]))
