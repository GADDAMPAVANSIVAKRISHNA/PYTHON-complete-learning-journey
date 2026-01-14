"""Demonstrate common string methods and practice examples."""


def title_case(s: str) -> str:
    return s.title()


# Practice (5):
# 1) Implement startswith/endswith checks without using builtins.
# 2) Count number of sentences in a paragraph.
# 3) Split a CSV line respecting quoted commas.
# 4) Implement a simple tokenization (split words, strip punctuation).
# 5) Implement case-insensitive substring search.

# Sample for 1:
def starts_with(s, prefix):
    return s[:len(prefix)] == prefix

if __name__ == "__main__":
    print(title_case('hello world from python'))
    print(starts_with('hello','he'))
