from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
r,c,d = map(int,stdin.readline().strip().split())

room = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
directions = [(0,-1),(1,0),(0,1),(-1,0)]

ans = 0

def clean(x,y):
    global ans,d
    if room[y][x] == 0:
        room[y][x] = 5
        ans+=1

    for _ in range(4):
        d = (d-1)%4
        dx,dy = directions[d]
        if room[y+dy][x+dx] == 0:
            return (x+dx,y+dy)
    
    dx,dy = directions[d]
    if room[y-dy][x-dx] == 1:
        return ()
    else:
        return (x-dx,y-dy)

while (l:=clean(c,r)):
    c,r = l

print(ans)
