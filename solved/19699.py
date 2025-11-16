from sys import stdin    

N,M = map(int,stdin.readline().strip().split())
H = list(map(int,stdin.readline().strip().split()))

arr = [0]*10001
for i in range(2,10001):
    for j in range(2*i,10001,i):
        arr[j]+=1

visited = [False]*N
ans = []
def solution(val=0,cnt=0):
    global N,M,H,ans,visited
    if cnt == M:
        if arr[val] == 0 and val not in ans:
            ans.append(val)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            solution(val+H[i],cnt+1)
            visited[i] = False

solution()
if ans:
    print(*sorted(ans))
else:
    print(-1)
