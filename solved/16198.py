from sys import stdin

N = int(stdin.readline().strip())
W = list(map(int,stdin.readline().strip().split()))
visited = [False]*N
ans = 0
def solution(l=N-2,val=0):
    global N,W,visited,ans
    if l == 0:
        ans = max(ans,val)
        return
    
    for i in range(1,N-1):
        if not visited[i]:
            tmp = 1
            for j in range(i-1,-1,-1):
                if not visited[j]:
                    tmp*=W[j]
                    break
            for k in range(i+1,N):
                if not visited[k]:
                    tmp*=W[k]
                    break
            visited[i] = True
            solution(l-1,val+tmp)
            visited[i] = False

solution()
print(ans)
