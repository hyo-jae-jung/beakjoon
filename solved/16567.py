from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
road = list(map(int,stdin.readline().strip().split()))
ans = []

cnt = 0 
p = 0
for i in road:
    if p == 0:
        if i == 1:
            cnt+=1
            p = 1
    else:
        if i == 0:
            p = 0

for _ in range(M):
    t = stdin.readline().strip()
    if t[0] == '1':
        idx = int(t[2:]) - 1
        if road[idx] == 1:
            continue
        else:
            a,b = 0,0
            if idx >= 1 and road[idx-1] == 1:
                a = 1
            if idx+1 < N and road[idx+1] == 1:
                b = 1
            
            if a + b == 2:
                cnt-=1
            elif a + b == 0:
                cnt+=1

            road[idx] = 1
    else:
        ans.append(cnt)

if ans:
    print(*ans,sep='\n')
