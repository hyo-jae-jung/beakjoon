from sys import stdin 

n = int(stdin.readline().strip())
ans = 0
for _ in range(n):
    h,w = map(int,stdin.readline().strip().split())
    ans = max(ans,h*w)

print(ans)
