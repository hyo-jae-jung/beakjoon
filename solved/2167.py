from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,stdin.readline().strip().split())))

K = int(stdin.readline().strip())
answer = []
accum_sum = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        accum_sum[i][j] = arr[i-1][j-1] + accum_sum[i-1][j] + accum_sum[i][j-1] - accum_sum[i-1][j-1]

for _ in range(K):
    x1,y1,x2,y2 = map(int,stdin.readline().strip().split())
    answer.append(accum_sum[x2][y2] - accum_sum[x1-1][y2] - accum_sum[x2][y1-1] + accum_sum[x1-1][y1-1])

print(*answer,sep='\n')
