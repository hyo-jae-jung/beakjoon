from sys import stdin 

ans = 0
n = int(stdin.readline().strip())
for _ in range(n):
    ans+=int(stdin.readline().strip())

print(ans)
