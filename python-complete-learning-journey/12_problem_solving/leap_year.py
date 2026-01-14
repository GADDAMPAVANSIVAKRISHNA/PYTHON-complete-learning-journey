"""Leap year checker and practice."""


def is_leap_year(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


# Practice (5):
# 1) Count leap years between two years inclusively.
# 2) Validate date inputs (e.g., ensure Feb 29 is valid).
# 3) Generate a list of leap years within a given range.
# 4) Determine next leap year from a given year.
# 5) Compute day-of-week for Feb 29 across a range.

# Sample solutions (example):
def count_leaps(a, b):
    return sum(1 for y in range(a, b+1) if is_leap_year(y))

if __name__ == "__main__":
    print(is_leap_year(2000), is_leap_year(1900), is_leap_year(2024))
    print('leaps 2000-2024', count_leaps(2000, 2024))
