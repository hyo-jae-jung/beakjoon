from sys import stdin  
from heapq import heapify, heappop

N = int(stdin.readline().strip())
a = list(map(int,stdin.readline().strip().split()))
heapify(a)
ans = [set()]

for _ in range(len(a)):

    i=0
    tmp = heappop(a)
    
    while True:
        
        if i == len(ans):
            ans.append(set())

        if tmp not in ans[i]:
            ans[i].add(tmp)
            break
        
        i+=1

print(len(ans))
