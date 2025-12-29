from sys import stdin  

R,C = map(int,stdin.readline().strip().split())
field = [list(stdin.readline().strip()) for _ in range(R)]

def dfs(X,Y):

    o,v = 0,0
    global field,R,C
    stack = [(X,Y)]
    fence = False
    while stack:
        x,y = stack.pop()
        if 0 == x or C-1 == x or 0 == y or R-1 == y:
            fence = True

        if field[y][x] == 'o':
            o+=1
        elif field[y][x] == 'v':
            v+=1
        field[y][x] = '#'

        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < C and 0 <= (ny:=y+dy) < R and field[ny][nx] != '#':
                stack.append((nx,ny))

    if fence:
        o,v = 0,0
    else:
        if o > v:
            v = 0
        else:
            o = 0
    return o,v

o,v = 0,0
for i in range(R):
    for j in range(C):
        if field[i][j] != '#':
            tmp_o,tmp_v = dfs(j,i)
            o+=tmp_o
            v+=tmp_v

print(o,v)
