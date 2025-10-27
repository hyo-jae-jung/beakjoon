from sys import stdin  
from heapq import heappop,heappush

N = int(stdin.readline().strip())
meetings = []
for _ in range(N):
    start,end = map(int,stdin.readline().strip().split())
    meetings.append((end,start))

meetings.sort(key=lambda x:(x[1],x[0]))
in_meetings = []
ans = 0
for end,start in meetings:

    while in_meetings and in_meetings[0][0] <= start:
        heappop(in_meetings)
    
    heappush(in_meetings,(end,start))
    ans = max(ans,len(in_meetings))

print(ans)
