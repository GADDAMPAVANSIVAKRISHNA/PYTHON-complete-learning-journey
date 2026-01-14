"""Operator examples and practice problems"""

# Practice (5):
# 1) Implement `is_even(n)` using bitwise operator.
# 2) Demonstrate operator precedence with an example.
# 3) Use bitwise operations to swap two integers without a temp variable.
# 4) Show short-circuit evaluation with `and`/`or` and side effects.
# 5) Compare identity (`is`) vs equality (`==`) behavior with small ints and objects.


def is_even(n: int) -> bool:
    return (n & 1) == 0

# Sample solution for 3 (swap using XOR):
def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == "__main__":
    print(is_even(10), is_even(11))
    print(1 + 2 * 3)  # precedence
    print('swap', swap_xor(5,7))
