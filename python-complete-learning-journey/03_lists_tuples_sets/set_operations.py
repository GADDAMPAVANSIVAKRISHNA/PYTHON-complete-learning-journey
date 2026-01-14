"""Set operations and practice problems."""


def common_elements(a, b):
    return list(set(a) & set(b))


# Practice (5):
# 1) Find elements unique to each of two lists.
# 2) Use sets to deduplicate while counting.
# 3) Use set operations to compute symmetric difference.
# 4) Implement subset/superset checks for permission sets.
# 5) Use frozen sets to create hashable collections.

if __name__ == "__main__":
    print(common_elements([1,2,3],[2,3,4]))
