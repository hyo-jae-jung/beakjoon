from sys import stdin   

N = int(stdin.readline().strip())
C = list(map(int,stdin.readline().strip().split()))
P = [[] for _ in range(N)]

for i in range(N):
    p = int(stdin.readline().strip())
    for _ in range(p):
        P[i].append(list(map(int,stdin.readline().strip().split())))

ans = float('inf')
visited = [False]*N
def solution(val=0,cnt=0):   
    global N,C,P,ans,visited
    if cnt == N:
        ans = min(ans,val)
        return 

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dc = C[i]
            tmp = C.copy()
            for j in P[i]:
                a,d = j
                a-=1
                if C[a] > d:C[a]-=d
                else:C[a] = 1
            solution(val+dc,cnt+1)
            C = tmp
            visited[i] = False

solution()
print(ans)
