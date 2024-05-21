from sys import stdin 

N = int(stdin.readline().strip())
menu = []
for _ in range(N):
    menu.append(int(stdin.readline().strip()))

ans = 0
M = int(stdin.readline().strip())
for _ in range(M):
    ans+=menu[int(stdin.readline().strip())-1]

print(ans)
