from sys import stdin 
from collections import defaultdict
from heapq import heappop,heappush

K,N = map(int,stdin.readline().strip().split())
d = defaultdict(list)
len_set = set()
for _ in range(K):
    temp = stdin.readline().strip()
    l = len(temp)
    len_set.add(l)
    heappush(d[l],-int(temp))

diff = N-K
len_list = sorted(list(len_set))

new_d = defaultdict(str)

for i in len_list:
    
