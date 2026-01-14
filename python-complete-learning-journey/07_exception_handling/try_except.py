"""Try / Except examples and practice"""


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# Practice (5):
# 1) Re-raise exceptions with additional context.
# 2) Use try/except/finally to ensure resource cleanup.
# 3) Implement a retry decorator for transient errors.
# 4) Log exceptions with traceback and context.
# 5) Write tests that assert exceptions are raised for invalid inputs.

if __name__ == "__main__":
    print(safe_divide(10,0))
