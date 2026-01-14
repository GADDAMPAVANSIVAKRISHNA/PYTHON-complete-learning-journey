"""Random module examples and practice."""

import random


def random_sample(lst, k):
    return random.sample(lst, k)


# Practice (5):
# 1) Shuffle a list in place and show reproducible sequences with seed.
# 2) Generate random passwords using choices or secrets.
# 3) Draw samples with and without replacement.
# 4) Simulate dice rolls and compute empirical distribution.
# 5) Use `secrets` for cryptographic randomness when needed.

if __name__ == "__main__":
    print(random_sample(list(range(10)), 3))
    import secrets
    print('secure token', secrets.token_hex(8))
