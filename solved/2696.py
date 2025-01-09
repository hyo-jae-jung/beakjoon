from sys import stdin  
from heapq import heappop, heappush 
from collections import deque

T = int(stdin.readline().strip())
ans_len,ans_arr = [],[]
for _ in range(T):
    M = int(stdin.readline().strip())
    A = deque()
    for _ in range((M//10) + 1):
        A.extend(deque(map(int,stdin.readline().strip().split())))

    arr,max_heap,min_heap = [],[],[]

    while A:
        tmp = A.popleft()
        if len(max_heap) == len(min_heap):
            heappush(max_heap,-tmp)
        else:
            heappush(min_heap,tmp)

        if min_heap:
            if -max_heap[0] > min_heap[0]:
                max_tmp = -heappop(max_heap)
                min_tmp = heappop(min_heap)

                heappush(max_heap,-min_tmp)
                heappush(min_heap,max_tmp)

        if len(max_heap) != len(min_heap):
            arr.append(-max_heap[0])

    ans_len.append(len(arr))
    ans_arr.append(arr)

for i in range(T):
    print(ans_len[i])
    for j in range(len(ans_arr[i])//10 + 1):
        print(*ans_arr[i][j*10:(j+1)*10])
