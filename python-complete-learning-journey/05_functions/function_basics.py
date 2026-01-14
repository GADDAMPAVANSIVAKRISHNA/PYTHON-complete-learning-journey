"""Function basics and practice problems."""


def greet(name='World'):
    return f"Hello, {name}!"


# Practice (5):
# 1) Write a function with *args to sum numbers.
# 2) Use default mutable arg correctly (avoid common pitfall).
# 3) Implement keyword-only arguments and validate them.
# 4) Create a decorator that logs function calls.
# 5) Use partial functions from functools for pre-filled args.

# Sample for 4 (simple decorator):
def log_calls(fn):
    def wrapper(*a, **kw):
        print('calling', fn.__name__)
        return fn(*a, **kw)
    return wrapper

@log_calls
def add(a,b):
    return a+b

if __name__ == "__main__":
    print(greet('Alice'))
    print(add(2,3))
