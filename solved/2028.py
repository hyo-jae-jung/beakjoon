from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = stdin.readline().strip()
    NN = int(N)**2
    if str(NN)[-len(N):] == N:
        ans.append('YES')
    else:
        ans.append('NO')

print(*ans,sep='\n')
