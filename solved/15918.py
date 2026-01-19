from sys import stdin  

n,x,y = map(int,stdin.readline().strip().split())
visited = [0]*(2*n)
fixed_val = y - x - 1
visited[x-1] = visited[y-1] = fixed_val
ans = 0
def solution(N=1):
    global n,x,y,visited,ans,fixed_val

    if N == fixed_val:
        solution(N+1)
        return

    if N > n:
        ans+=1
        return 

    for i in range(2*n):
        if not visited[i] and i+N+1 < 2*n and not visited[i+N+1]:
            visited[i] = visited[i+N+1] = N
            solution(N+1)
            visited[i] = visited[i+N+1] = 0

solution()
print(ans)
