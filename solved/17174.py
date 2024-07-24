from sys import stdin  

N,M = map(int,stdin.readline().strip().split())

ans = 0
while N > 0:
    ans+=N
    N = N//M

print(ans)
