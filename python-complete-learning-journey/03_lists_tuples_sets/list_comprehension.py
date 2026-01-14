"""List comprehension examples and practice."""


def squares_up_to(n):
    return [i*i for i in range(n+1)]


# Practice (5):
# 1) Use nested comprehensions for matrix flattening.
# 2) Create a dict comprehension for frequency counts.
# 3) Create a list of tuples with filters and transformations.
# 4) Use comprehension with conditional expression.
# 5) Convert a comprehension into an equivalent for-loop and compare.

if __name__ == "__main__":
    print(squares_up_to(5))
    print([x for x in range(10) if x%2==0])
