from sys import stdin   

M = int(stdin.readline().strip())

MOD = 10**9 + 7

N = 4_000_000
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

ans = []

for _ in range(M):
    N,K = map(int,stdin.readline().strip().split())
    ans.append(comb(N,K)%MOD)

print(*ans,sep="\n")
