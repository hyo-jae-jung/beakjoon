from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    for _ in range(N):
        A,B = map(int,stdin.readline().strip().split())
        ans.append((A+B,A*B))

for i in ans:
    print(*i)
