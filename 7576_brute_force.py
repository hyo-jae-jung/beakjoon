import time
from collections import deque

start = time.time()

M,N = input().split()
tomato_box = [deque(map(int,input().split())) for _ in range(int(N))]

for i in tomato_box:
    i.insert(0,0)
    i.append(0)

tomato_box.insert(0,[0]*(int(M)+2))
tomato_box.append([0]*(int(M)+2))

day = 0

while True:
    local_list = deque([])
    for i in range(1,int(N)+1):
        for j in range(1,int(M)+1):
            if tomato_box[i][j] not in [-1,1]:
                if 1 in [tomato_box[i-1][j],tomato_box[i][j-1],tomato_box[i+1][j],tomato_box[i][j+1]]:
                    local_list.append([i,j])
    
    for i,j in local_list:
        tomato_box[i][j] = 1

    if len(local_list) == 0:
        if 0 in tomato_box[1:int(N)+1][1:int(M)+1]:
            day = -1
        break
    day += 1
end = time.time()
print(day)
print(end-start)
"""
map
np.array
insert

ideas
if 많이 쓰기 싫어서 상자의 둘레를 0으로 padding
체크하는 도중  토마토가 익어버리면 익은 토마토로 간주하기 때문에 체크와 변화는 따로 해야함
"""