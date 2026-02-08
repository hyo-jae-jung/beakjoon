from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
ans = -1
problems = []
for _ in range(M):
    problems.append(sum(map(lambda x:1 << (x-1),list(map(int,stdin.readline().strip().split()))[1:])))
visited = [True]*M

def solution(idx=0,val=0,cnt=0):
    global N,M,problems,visited,ans
    if (1 << N) - 1 == val:
        if ans == -1:
            ans = cnt
        else:
            ans = min(ans,cnt)
        return 
    
    for i in range(idx,M):
        if visited[i]:
            visited[i] = False
            solution(i+1,val | problems[i],cnt+1)
            visited[i] = True

solution()
print(ans)
