"""Type casting examples and practice problems."""

def to_int_safe(s: str, default=0):
    try:
        return int(s)
    except ValueError:
        return default


# Practice (5):
# 1) Convert a mixed list ['1', '2', 'three'] to ints safely.
# 2) Demonstrate float -> int rounding behavior and differences (floor vs round).
# 3) Safely cast nested lists/dicts values when possible.
# 4) Parse numbers with thousands separators and different locales.
# 5) Implement a generic `safe_cast(obj, type, default)` helper and test it.

# Sample solution (example for 1):
def convert_list_to_ints(lst, default=0):
    return [to_int_safe(x, default) for x in lst]

if __name__ == "__main__":
    print(to_int_safe('123'))
    print(to_int_safe('abc', default=-1))
    print(convert_list_to_ints(['1','2','three']))
