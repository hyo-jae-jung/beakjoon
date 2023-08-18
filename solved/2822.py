from sys import stdin 
from heapq import heappop,heappush

scores = []
tmp = []
answer = []
for i in range(1,9):
    heappush(scores,(-int(stdin.readline().strip()),i))

max_total_values = 0
for _ in range(5):
    value,idx = heappop(scores)
    max_total_values-=value
    heappush(tmp,idx)

for _ in range(5):
    answer.append(heappop(tmp))

print(max_total_values)
print(*answer)
