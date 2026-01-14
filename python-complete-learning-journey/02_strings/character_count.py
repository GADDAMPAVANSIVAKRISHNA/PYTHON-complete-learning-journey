"""Count characters and frequency examples."""

from collections import Counter


def char_frequency(s: str) -> dict:
    return dict(Counter(s))


# Practice (5):
# 1) Return top 3 most frequent characters.
# 2) Normalize case and count letters only.
# 3) Count words and return most common words.
# 4) Use sliding window to count substrings of length k.
# 5) Implement frequency using dict vs Counter and compare.

# Sample solution for 1 and 2:
def top_k_chars(s, k=3):
    c = Counter(ch.lower() for ch in s if ch.isalpha())
    return c.most_common(k)

if __name__ == "__main__":
    print(char_frequency('abracadabra'))
    print(top_k_chars('Hello Hello!!', 2))
