"""While loop examples"""

def countdown(n):
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result


# Practice (5):
# 1) Implement a function to find greatest common divisor using while loop.
# 2) Use while loop to read inputs until a sentinel value.
# 3) Implement an integer square root using while loops.
# 4) Use while with else to find an item or conclude not found.
# 5) Implement an exponential search (growing step-size) using while.

if __name__ == "__main__":
    print(countdown(5))
    def gcd(a,b):
        while b:
            a,b = b, a%b
        return a
    print('gcd 48 18 =', gcd(48,18))
