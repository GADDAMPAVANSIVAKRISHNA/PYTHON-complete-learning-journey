"""Dictionary basics and practice problems."""


def invert_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}


# Practice (5):
# 1) Merge dictionaries with conflict resolution.
# 2) Build a frequency counter from a string.
# 3) Flatten a nested dict with dot-separated keys.
# 4) Group a list of pairs into a dict of lists.
# 5) Implement a LRU cache using dict and order.

if __name__ == "__main__":
    print(invert_dict({'a':1,'b':2}))
    print('grouped', {k:[v for (x,v) in [('a',1),('a',2)] if x==k] for k in ['a']})
