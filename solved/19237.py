from sys import stdin  

N,M,k = map(int,stdin.readline().strip().split())
graph = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

shark_directions = [0] + list(map(int,stdin.readline().strip().split()))
shark_locations = []
direction_map = {}
for i in range(1,M+1):
    direction_map.update({i:[]})
    for j in range(4):
        direction_map[i].append(list(map(int,stdin.readline().strip().split())))

def arrange_direction(shark_num):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    ans = []
    for i in direction_map[shark_num][shark_directions[shark_num]-1]:
        ans.append((*directions[i-1],i))
    return ans

scent_map = [[0]*N for _ in range(N)]
scent_info = {}

for i in range(N):
    for j in range(N):
        if graph[i][j] > 0:
            shark_locations.append((graph[i][j],i,j))
            scent_map[i][j] = graph[i][j]
            scent_info.update({(i,j):k})

shark_locations.sort()

def shark_move(shark_num,y,x):
    empty = []
    my_scent = []
    for dy,dx,num in arrange_direction(shark_num):
        if 0 <= (nx:=x+dx) < N and 0 <= (ny:=y+dy) < N:
            if graph[ny][nx] == 0 and scent_map[ny][nx] == 0:
                empty.append((ny,nx,num))
            elif scent_map[ny][nx] == shark_num:
                my_scent.append((ny,nx,num))
    if empty:
        return shark_num,*empty[0]
    return shark_num,*my_scent[0]

ans = 0

while len(shark_locations) > 1 and ans <= 1000:

    action = []

    for shark_number,y,x in shark_locations:
        shark_num,y,x,dir_num = shark_move(shark_number,y,x)
        shark_directions[shark_num] = dir_num
        action.append((shark_num,y,x))

    for key,value in scent_info.items():
        scent_info[key]-=1
    for key in [key for key,value in scent_info.items() if value == 0]:
        del scent_info[key]
        scent_map[key[0]][key[1]] = 0

    new = []
    for a,b in zip(action,shark_locations):
        if graph[a[1]][a[2]] == 0:
            graph[a[1]][a[2]] = a[0]
            scent_map[a[1]][a[2]] = a[0]
            if scent_info.get((a[1],a[2])):
                scent_info[(a[1],a[2])] = k
            else:
                scent_info.update({(a[1],a[2]):k})
            new.append(a)
        graph[b[1]][b[2]] = 0

    shark_locations = new
    ans+=1

print(ans if ans <= 1000 else -1)
