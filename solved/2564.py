from sys import stdin  

col,row = map(int,stdin.readline().strip().split())
n = int(stdin.readline().strip())
shops = [tuple(map(int,stdin.readline().strip().split())) for _ in range(n)]
dongun = tuple(map(int,stdin.readline().strip().split()))

road = []

for i in range(col):
    road.append((i,0))
for i in range(row+1):
    road.append((col,i))
for i in range(col-1,-1,-1):
    road.append((i,row))
for i in range(row-1,0,-1):
    road.append((0,i))

road_l = len(road)

def xy_point(t:tuple):
    if t[0] == 1:
        return (t[1],0)
    if t[0] == 2:
        return (t[1],row)
    if t[0] == 3:
        return (0,t[1])
    if t[0] == 4:
        return (col,t[1])
    
def distance(t_idx,t2,direction):
    cnt = 0
    while road[t_idx] != t2:
        t_idx = (t_idx+direction)%road_l
        cnt+=1
    return cnt

new_dongun = xy_point(dongun)

ans = 0
for t in shops:
    tmp_i = road.index(xy_point(t))
    ans+=min(distance(tmp_i,new_dongun,1),distance(tmp_i,new_dongun,-1))

print(ans)
