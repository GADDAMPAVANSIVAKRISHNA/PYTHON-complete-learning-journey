"""Basic string operations and practice problems."""


def reverse_string(s: str) -> str:
    return s[::-1]


# Practice (5):
# 1) Count characters, words and lines in a string.
# 2) Implement a function that capitalizes every word.
# 3) Find the most common word in a paragraph.
# 4) Implement simple text normalization (lowercase, strip punctuation).
# 5) Detect and extract email addresses from text using simple parsing.

if __name__ == "__main__":
    print(reverse_string('abcde'))
    s = 'Hello world. Hello!'
    from collections import Counter
    print('most common', Counter(s.split()).most_common(1))
