"""Common dictionary methods and exercises."""


def merge_with_sum(d1, d2):
    res = d1.copy()
    for k, v in d2.items():
        res[k] = res.get(k, 0) + v
    return res


# Practice (5):
# 1) Use defaultdict to group items.
# 2) Convert list of pairs into a dictionary.
# 3) Merge dictionaries with custom conflict resolvers.
# 4) Implement nested dict set/get helpers.
# 5) Swap keys and values with collision handling.

if __name__ == "__main__":
    print(merge_with_sum({'a':1,'b':2},{'b':3,'c':4}))
