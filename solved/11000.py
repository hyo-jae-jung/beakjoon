from sys import stdin  
from heapq import heappop,heappush
N = int(stdin.readline().strip())
lectures = []
for _ in range(N):
    s,t = map(int,stdin.readline().strip().split())
    lectures.append((t,s))

lectures.sort(key=lambda x:(x[1],x[0]))
in_lectures = []
ans = 0

for lecture in lectures:

    while in_lectures and in_lectures[0][0] <= lecture[1]:
        heappop(in_lectures)

    heappush(in_lectures,lecture)
    ans = max(ans,len(in_lectures))

print(ans)
