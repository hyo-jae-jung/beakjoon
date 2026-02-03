from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
track = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

visited = [[float('inf')]*M for _ in range(N)]
visited[0][0] = 0

for i in range(N):
    for j in range(M):
        for dx in range(1,min(track[i][j]+1,M-j)):
            if visited[i][j+dx] > visited[i][j]:
                visited[i][j+dx] = visited[i][j] + 1

        for dy in range(1,min(track[i][j]+1,N-i)):
            if visited[i+dy][j] > visited[i][j]:
                visited[i+dy][j] = visited[i][j] + 1

print(visited[-1][-1])
