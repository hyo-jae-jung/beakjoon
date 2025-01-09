from sys import stdin 
from heapq import heappop, heappush

N = int(stdin.readline().strip())

ans,max_heap,min_heap = [],[],[]

for _ in range(N):
    tmp = int(stdin.readline().strip())
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
    ans.append(-max_heap[0])

print(*ans,sep='\n')
