from sys import stdin   

n,r = map(int,stdin.readline().strip().split())

MOD = 10**9 + 7

N = 1000000
fact = [1] * (N + 1)
ifact = [1] * (N + 1)

for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % MOD


ifact[N] = pow(fact[N], MOD - 2, MOD)
for i in range(N - 1, 0, -1):
    ifact[i] = ifact[i + 1] * (i + 1) % MOD


def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD

print(comb(n, r))
