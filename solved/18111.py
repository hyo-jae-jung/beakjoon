from sys import stdin 

N,M,B = map(int,stdin.readline().strip().split())
earth = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

min_floor = float('inf')
max_floor = 0

for i in range(N):
    for j in range(M):
        min_floor = min(min_floor,earth[i][j])
        max_floor = max(max_floor,earth[i][j])

ans = []
for k in range(min_floor,max_floor+1):
    b = B
    t = 0
    for i in range(N):
        for j in range(M):
            tmp = earth[i][j] - k
            if tmp > 0:
                t+=tmp*2
                b+=tmp
            elif tmp < 0:
                t-=tmp
                b+=tmp
    if b < 0:
        continue
    ans.append((t,k))

ans.sort(key=lambda x:(x[0],-x[1]))

print(*ans[0])
