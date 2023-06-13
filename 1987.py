import sys
sys.setrecursionlimit(10**4)

R,C = map(int,sys.stdin.readline().strip().split())
chart = []
for _ in range(R):
    chart.append(list(sys.stdin.readline().strip()))

max_distance = 0
s = set()

def dfs(x=0,y=0,cnt=1):

    global max_distance
    max_distance = max(max_distance,cnt)

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < C and 0 <= ny < R and not chart[ny][nx] in s:
            s.add(chart[ny][nx])
            dfs(nx,ny,cnt+1)
            s.remove(chart[ny][nx])

s.add(chart[0][0])
dfs()
print(max_distance)
