"""Demonstrate finally and else in exception handling."""


def read_int(s):
    try:
        n = int(s)
    except ValueError:
        return None
    else:
        return n
    finally:
        pass


# Practice (5):
# 1) Use finally to close resources (e.g., files).
# 2) Show how else only runs when no exception occurs.
# 3) Demonstrate that finally executes even when returning inside try/except.
# 4) Use try/except/else/finally for safe resource management.
# 5) Implement a small context manager that logs entry/exit to show finally-like behavior.

if __name__ == "__main__":
    print(read_int('10'), read_int('x'))
