"""Variables and datatypes examples and short practice problems.

Practice (5):
1) Implement `swap(a,b)` that returns (b,a).
2) Count vowels in a string.
3) Implement a function to detect data type homogeneity in a list.
4) Convert a list of strings to typed values based on hints.
5) Detect and coerce numeric strings inside a nested structure.

Sample solutions (examples):
def swap(a, b):
    """Return values swapped"""
    return b, a


def count_vowels(s: str) -> int:
    """Return number of vowels in the string."""
    return sum(1 for ch in s.lower() if ch in 'aeiou')

# Example solution for 3:
def is_homogeneous(lst):
    return all(type(x) is type(lst[0]) for x in lst) if lst else True

if __name__ == "__main__":
    print(swap(1, 2))
    print(count_vowels("Hello World"))
    print(is_homogeneous([1,2,3]), is_homogeneous([1,'a']))
