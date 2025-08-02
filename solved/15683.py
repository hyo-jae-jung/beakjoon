from sys import stdin   
from copy import deepcopy

N,M = map(int,stdin.readline().strip().split())
room = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

cctv_info = []
for i in range(N):
    for j in range(M):
        if 0 < room[i][j] < 6:
            cctv_info.append((i,j,room[i][j]))

def cctv1(room,y,x):
    ans = []
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        arr = deepcopy(room)
        for i in range(1,max(N,M)):
            if 0 <= (nx:=x+dx*i) < M and 0 <= (ny:=y+dy*i) < N:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = '#'
                elif arr[ny][nx] == '#' or 0 < arr[ny][nx] < 6:
                    continue
                elif arr[ny][nx] == 6:
                    ans.append(arr)
                    break
            else:
                ans.append(arr)
                break
        else:
            ans.append(arr)

    return ans

def cctv2(room,y,x):
    ans = []
    directions = [[(-1,0),(1,0)],[(0,-1),(0,1)]]
    for i in directions:
        arr = deepcopy(room)
        for dx,dy in i:
            for i in range(1,max(N,M)):
                if 0 <= (nx:=x+dx*i) < M and 0 <= (ny:=y+dy*i) < N:
                    if arr[ny][nx] == 0:
                        arr[ny][nx] = '#'
                    elif arr[ny][nx] == '#' or 0 < arr[ny][nx] < 6:
                        continue
                    elif arr[ny][nx] == 6:
                        break
                else:
                    break
        ans.append(arr)
    return ans

def cctv3(room,y,x):
    ans = []
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    for i in range(4):
        arr = deepcopy(room)
        for j in range(2):
            dx,dy = directions[(i+j)%4]
            for k in range(1,max(N,M)):
                if 0 <= (nx:=x+dx*k) < M and 0 <= (ny:=y+dy*k) < N:
                    if arr[ny][nx] == 0:
                        arr[ny][nx] = '#'
                    elif arr[ny][nx] == '#' or 0 < arr[ny][nx] < 6:
                        continue
                    elif arr[ny][nx] == 6:
                        break
                else:
                    break
        ans.append(arr)
    return ans

def cctv4(room,y,x):
    ans = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(4):
        arr = deepcopy(room)
        for j,d in enumerate(directions):
            if j == i:
                continue
            dx,dy = d
            for k in range(1,max(N,M)):
                if 0 <= (nx:=x+dx*k) < M and 0 <= (ny:=y+dy*k) < N:
                    if arr[ny][nx] == 0:
                        arr[ny][nx] = '#'
                    elif arr[ny][nx] == '#' or 0 < arr[ny][nx] < 6:
                        continue
                    elif arr[ny][nx] == 6:
                        break
                else:
                    break
        ans.append(arr)
    return ans

def cctv5(room,y,x):
    ans = []
    arr = deepcopy(room)
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        for i in range(1,max(N,M)):
            if 0 <= (nx:=x+dx*i) < M and 0 <= (ny:=y+dy*i) < N:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = '#'
                elif arr[ny][nx] == '#' or 0 < arr[ny][nx] < 6:
                    continue
                elif arr[ny][nx] == 6:
                    break
            else:
                break
    ans.append(arr)
    return ans

room_info = [room]

while cctv_info:
    y,x,num = cctv_info.pop()
    new_room_info = []
    while room_info:
        arr = room_info.pop()
        if num == 1:
            new_room_info.extend(cctv1(arr,y,x))
        if num == 2:
            new_room_info.extend(cctv2(arr,y,x))
        if num == 3:
            new_room_info.extend(cctv3(arr,y,x))
        if num == 4:
            new_room_info.extend(cctv4(arr,y,x))
        if num == 5:
            new_room_info.extend(cctv5(arr,y,x))
    
    room_info = new_room_info

ans = float('inf')

for i in room_info:
    tmp_cnt = 0
    for j in range(N):
        for k in range(M):
            if i[j][k] == 0:
                tmp_cnt+=1
    ans = min(ans,tmp_cnt)

print(ans)
