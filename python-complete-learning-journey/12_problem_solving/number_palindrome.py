"""Number palindrome checks and practice."""


def is_number_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


# Practice (5):
# 1) Find largest palindrome product of two 3-digit numbers.
# 2) Generate palindrome primes within a range.
# 3) Check if a numeric series contains palindromic subsequences.
# 4) Compute next palindrome greater than a given number.
# 5) Find palindrome pairs in a list of numbers (a+b forms palindrome).
#
# Sample solutions (examples):
def next_palindrome(n):
    while True:
        n += 1
        if is_number_palindrome(n):
            return n

if __name__ == "__main__":
    print(is_number_palindrome(121), is_number_palindrome(123))
    print('next palindrome after 123 =', next_palindrome(123))
