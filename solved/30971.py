from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split())) + [0]
B = list(map(int,stdin.readline().strip().split())) + [0]
C = list(map(int,stdin.readline().strip().split())) + [0]
visited = [False]*N
ans = -1

def solution(before=N,cnt=0,val=0):
    global N,K,A,B,C,visited,ans
    if cnt == N:
        ans = max(ans,val)
        return
    
    for i in range(N):
        if not visited[i]:
            if C[before]*C[i] <= K:
                visited[i] = True
                solution(i,cnt+1,val+A[before]*B[i])
                visited[i] = False

solution()
print(ans)
