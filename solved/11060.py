from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())
A = [int(i) for i in stdin.readline().strip().split()]

queue = deque([(0,0)])
memo = [0]*N
while queue:
    temp = queue.popleft()
    if temp[0] == (N-1):
        print(temp[1])
        break

    for i in range(1,A[temp[0]]+1):
        next_idx = temp[0]+i
        next_cnt = temp[1]+1
        if next_idx < N:
            if not memo[next_idx]:
                memo[next_idx] = next_cnt
                queue.append((next_idx,next_cnt))
            else:
                if memo[next_idx] > next_cnt:
                    queue.append((next_idx,next_cnt))
        else:
            break
else:
    print(-1)
