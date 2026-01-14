"""Examples of arguments and return values."""


def divide(a, b):
    if b == 0:
        raise ValueError('division by zero')
    return a / b


# Practice (5):
# 1) Implement a function that returns multiple results (quotient,remainder).
# 2) Write a function that accepts keyword-only args.
# 3) Use variable-length args and keywords to accept arbitrary parameters.
# 4) Demonstrate tuple unpacking of returned values.
# 5) Implement function overloading behavior using singledispatch.

if __name__ == "__main__":
    print(divide(10,2))
    def divmod_pair(a,b):
        return a//b, a%b
    print(divmod_pair(10,3))
