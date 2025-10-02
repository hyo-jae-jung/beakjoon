from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N,M = map(int,stdin.readline().strip().split())
    for _ in range(M):
        stdin.readline().strip()
    ans.append(N-1)

print(*ans,sep='\n')
