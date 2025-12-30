def is_palindrome(n:str):
    for i in range(len(n)//2):
        if n[i] != n[-(1+i)]:
            return False
    return True

def linear_sieve(n):
    primes = []
    min_prime = [0] * (n + 1)

    for i in range(2, n + 1):
        if min_prime[i] == 0:
            min_prime[i] = i
            primes.append(i)

        for p in primes:
            if p > min_prime[i] or i * p > n:
                break
            min_prime[i * p] = p

    return primes

primes = linear_sieve(1003001)
pal_primes = []
for prime in primes:
    if is_palindrome(str(prime)):
        pal_primes.append(prime)

from sys import stdin  
from bisect import bisect_left

N = int(stdin.readline().strip())
idx = bisect_left(pal_primes,N)

print(pal_primes[idx])
