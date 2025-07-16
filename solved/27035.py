from sys import stdin  

N = int(stdin.readline().strip())
bulls = []
for _ in range(N):
    bulls.append(int(stdin.readline().strip()))
girls = []
for _ in range(N):
    girls.append(int(stdin.readline().strip()))

ans = 0
for i,j in zip(sorted(bulls),sorted(girls)):
    ans+=abs(i-j)

print(ans)
