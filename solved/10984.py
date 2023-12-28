from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    up = 0
    down = 0
    for _ in range(N):
        C,G = stdin.readline().strip().split()
        up+=int(C)*float(G)
        down+=int(C)
    ans.append((down,round(up/down,1)))

for i in ans:
    print(*i)
