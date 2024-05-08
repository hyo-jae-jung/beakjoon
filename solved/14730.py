from sys import stdin 

N = int(stdin.readline().strip())
ans = 0
for _ in range(N):
    C,K = map(int,stdin.readline().strip().split())
    ans+=C*K

print(ans)
