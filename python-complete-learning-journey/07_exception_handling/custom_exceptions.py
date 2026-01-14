"""Custom exception examples."""

class InvalidAgeError(ValueError):
    pass


def set_age(a):
    if a < 0:
        raise InvalidAgeError('age cannot be negative')
    return a


# Practice (5):
# 1) Define and raise custom exceptions for domain errors.
# 2) Catch multiple exception types in one except block.
# 3) Create a hierarchy of custom exceptions (e.g., DataError -> ValidationError).
# 4) Attach metadata to exceptions and serialize them (for logging/reporting).
# 5) Implement validation functions that raise specific custom exceptions.

# Sample snippet (example for 3):
class ValidationError(Exception):
    pass

if __name__ == "__main__":
    try:
        set_age(-1)
    except InvalidAgeError as e:
        print('caught', e)
