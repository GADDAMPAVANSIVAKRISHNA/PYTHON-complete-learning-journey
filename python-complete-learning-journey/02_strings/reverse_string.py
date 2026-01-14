"""Reverse string examples and practice"""

def reverse_iterative(s: str) -> str:
    out = ''
    for ch in s:
        out = ch + out
    return out


# Practice (5):
# 1) Reverse words in a sentence (not just characters).
# 2) Check if two strings are rotations of each other.
# 3) Reverse only letters in a string leaving positions of non-letters.
# 4) Reverse lines of a paragraph while keeping line order.
# 5) Implement reverse using recursion.

# Sample solution for 1:
def reverse_words(s):
    return ' '.join(s.split()[::-1])

if __name__ == "__main__":
    print(reverse_iterative('hello'))
    print(reverse_words('hello world'))
