from sys import stdin 

N = int(stdin.readline().strip())
ans = 1
for _ in range(N):
    ans+=int(stdin.readline().strip())-1

print(ans)
