from sys import stdin   

R,C = map(int,stdin.readline().strip().split())
arr = [list(stdin.readline().strip()) for _ in range(R)]

def sink(x,y):
    sea_cnt = 0
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx = x+dx
        ny = y+dy
        if nx < 0 or nx >= C or ny < 0 or ny >= R:
            sea_cnt+=1
        else:
            if arr[ny][nx] == '.':
                sea_cnt+=1
    
    if sea_cnt >= 3:
        return True
    return False
    
stack = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X' and sink(j,i):
            stack.append((j,i))

while stack:
    x,y = stack.pop()    
    arr[y][x] = '.'

new_x_loc = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            new_x_loc.append((j,i))

max_col = 0
min_col = float('inf')
max_row = 0
min_row = float('inf')

for x,y in new_x_loc:
    max_col = max(max_col,y)
    min_col = min(min_col,y)
    max_row = max(max_row,x)
    min_row = min(min_row,x)

for i in range(min_col,max_col+1):
    tmp = ''
    for j in range(min_row,max_row+1):
        tmp+=arr[i][j]
    print(tmp)
