from sys import stdin 

N = int(stdin.readline().strip())

work_time = []
for _ in range(N):
    start,end = map(int,stdin.readline().strip().split())
    work_time.append([60*(start//100)+start%100-10,60*(end//100)+end%100+10])

work_time.sort(key=lambda x:(x[0],x[1]))
work_time.append([1320,1320])

stack = 600
ans = 0

for i in range(N+1):
    if work_time[i][0] >= stack:
        ans = max(ans,work_time[i][0] - stack)

    if work_time[i][1] > stack:
        stack = work_time[i][1]
    
print(ans)
