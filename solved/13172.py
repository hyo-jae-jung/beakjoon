from sys import stdin    

M = int(stdin.readline().strip())
ans = 0
for _ in range(M):
    n,s = map(int,stdin.readline().strip().split())
    ans+=(s*pow(n,10**9+5,10**9+7))%(10**9+7)

print(ans%(10**9+7))
