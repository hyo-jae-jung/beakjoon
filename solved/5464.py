from sys import stdin  
from collections import deque 

N,M = map(int,stdin.readline().strip().split())
parking_lot = [0]*N
cost_per_weight = [int(stdin.readline().strip()) for _ in range(N)]
cars = [int(stdin.readline().strip()) for _ in range(M)]
q = deque()
cars_loc = {}
rest_cnt = N
ans = 0
for _ in range(2*M):
    num_and_vector = int(stdin.readline().strip())
    if num_and_vector > 0:
        q.append(num_and_vector)
    else:
        ans+=parking_lot[cars_loc[-num_and_vector]]
        parking_lot[cars_loc[-num_and_vector]] = 0
        rest_cnt+=1

    if rest_cnt > 0 and q:
        nav = q.popleft()
        for i in range(N):
            if parking_lot[i] == 0:
                parking_lot[i] = cars[nav-1]*cost_per_weight[i]
                cars_loc.update({nav:i})
                rest_cnt-=1
                break
    
print(ans)
