import sys
sys.setrecursionlimit(10**3)

R,C = map(int,sys.stdin.readline().strip().split())
chart = []
for _ in range(R):
    chart.append(list(sys.stdin.readline().strip()))
temp = set(sum(chart,[]))
max_l = len(temp)
max_distance = 0
d = [False]*26
def dfs(x=0,y=0,cnt=1):

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < C and 0 <= ny < R and not d[ord(chart[ny][nx])-65]:
            d[ord(chart[ny][nx])-65] = True
            dfs(nx,ny,cnt+1)
            d[ord(chart[ny][nx])-65] = False
        else:
            global max_distance
            max_distance = max(max_distance,cnt)
            if max_distance == max_l:
                return True

d[ord(chart[0][0])-65] = True
dfs()
print(max_distance)
