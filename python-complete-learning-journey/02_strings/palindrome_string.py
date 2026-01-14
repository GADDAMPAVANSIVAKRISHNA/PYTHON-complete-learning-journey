"""Palindrome related functions and practice."""

def is_palindrome(s: str) -> bool:
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s2 == s2[::-1]


# Practice (5):
# 1) Check numeric palindrome for integer.
# 2) Longest palindromic substring (challenge).
# 3) Count palindromic substrings in a string.
# 4) Check if any permutation of a string is a palindrome.
# 5) Use expand-around-center to implement longest palindrome.

# Sample solution for 1 (number):
def is_num_pal(n):
    s = str(n)
    return s == s[::-1]

if __name__ == "__main__":
    print(is_palindrome('A man, a plan, a canal: Panama'))
    print(is_num_pal(1221))
