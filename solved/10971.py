from sys import stdin   

N = int(stdin.readline().strip())
road = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

visited = [False]*N
ans = float('inf')

def solution(start=-1,prev=-1,cnt=0,val=0):
    global N,road,visited,ans
    if cnt == N and road[prev][start] > 0:
        ans = min(ans,val+road[prev][start])
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            if cnt == 0:
                start = i
                prev = i
                solution(start,i,cnt+1,val)
            if road[prev][i] > 0:
                solution(start,i,cnt+1,val+road[prev][i])
            if cnt == 0:
                start = -1
                prev = -1
            visited[i] = False

solution()
print(ans)
