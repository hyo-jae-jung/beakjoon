from sys import stdin  

T = int(stdin.readline().strip())
ans = 0
for _ in range(T):
    ans+=int(stdin.readline().strip())

print(ans)
