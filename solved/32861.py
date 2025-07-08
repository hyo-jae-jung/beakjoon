from sys import stdin  

N = int(stdin.readline().strip())
A = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

def solution():

    indegree = [N]*N
    
    for i in range(N):
        if A[i][i] != 0:
            return None
        for j in range(1+i,N):

            if A[i][j] == 0 or A[j][i] == 0:
                return None
            
            if A[i][j] + A[j][i] != 0:
                return None

            if A[i][j] == 1:
                indegree[i]-=1
            if A[i][j] == -1:
                indegree[j]-=1

    return indegree

ans = solution()

if ans is not None and sorted(ans) == list(range(1,N+1)):
    print(*ans)
else:
    print(-1)
