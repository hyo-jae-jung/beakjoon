from sys import stdin  

N,B = map(int,stdin.readline().strip().split())
stacks = [int(stdin.readline().strip()) for _ in range(N)]

visited = [False]*N
ans = float('inf')

def solution(diff=-B,idx=0):
    global N,stacks,visited,ans
    if diff >= 0:
        ans = min(ans,diff)
        return 
    
    if ans == 0:
        return

    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            solution(diff+stacks[i],i+1)
            visited[i] = False

solution()
print(ans)
