from sys import stdin 

N = int(stdin.readline().strip())
ans = 0
for _ in range(N):
    a,b = map(int,stdin.readline().strip().split())
    t = ans%(a+b)
    ans+=(b-t if b>=t else 0) + 1

print(ans)
