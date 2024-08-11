from sys import stdin  

N = int(stdin.readline().strip())
ans = 0
for _ in range(N):
    a,d,g = map(int,stdin.readline().strip().split())
    ans = max(ans,a*(d+g) if a != d+g else a*(d+g)*2)

print(ans)
