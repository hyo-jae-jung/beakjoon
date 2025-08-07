from sys import stdin  

N = int(stdin.readline().strip())
move = stdin.readline().strip()

directions = [(-1,0),(0,1),(1,0),(0,-1)]
direction = 1

diff = [0,0,0,0]

loc = (0,0)
for i in move:
    if i == 'R':
        direction = (direction-1)%4
    elif i == 'L':
        direction = (direction+1)%4
    elif i == 'F':
        loc = (loc[0]+directions[direction][0],loc[1]+directions[direction][1])
        diff[0] = max(loc[0],diff[0])
        diff[1] = max(loc[1],diff[1])
        diff[2] = min(loc[0],diff[2])
        diff[3] = min(loc[1],diff[3])

col = diff[0] - diff[2] + 1
row = diff[1] - diff[3] + 1

start_loc = (0-diff[2],0-diff[3])

graph = [['#']*col for _ in range(row)]
graph[start_loc[1]][start_loc[0]] = '.'
direction = 1
for i in move:
    if i == 'R':
        direction = (direction-1)%4
    elif i == 'L':
        direction = (direction+1)%4
    elif i == 'F':
        start_loc = (start_loc[0]+directions[direction][0],start_loc[1]+directions[direction][1])
    graph[start_loc[1]][start_loc[0]] = '.'

for i in graph:
    print(''.join(i))
