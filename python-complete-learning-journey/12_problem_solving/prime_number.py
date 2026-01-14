"""Prime related checks and practice."""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# Practice (5):
# 1) Sieve of Eratosthenes to generate primes up to N.
# 2) Prime factorization returning factor counts.
# 3) Use Miller–Rabin test for large primes (research exercise).
# 4) Find twin primes in a given range.
# 5) Count primes in an interval efficiently.

# Sample solution (sieve):
def sieve(n):
    sieve = [True]*(n+1)
    sieve[0:2] = [False, False]
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]

if __name__ == "__main__":
    print([n for n in range(1,20) if is_prime(n)])
    print('primes to 30:', sieve(30))
