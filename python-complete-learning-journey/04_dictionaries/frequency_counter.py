"""Frequency counter examples."""

from collections import Counter


def most_common_k(items, k=3):
    return Counter(items).most_common(k)


# Practice (5):
# 1) Count words in a text and show top 5.
# 2) Use Counter to subtract counts between two datasets.
# 3) Find elements with frequency above a threshold.
# 4) Merge counters and show normalized frequencies.
# 5) Use sliding window frequency counts.

if __name__ == "__main__":
    print(most_common_k(['a','b','a','c','a','b'], 2))
