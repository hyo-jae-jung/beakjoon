from sys import stdin 

T,W = map(int,stdin.readline().strip().split())

cnt = 0
num = 0
arr = []

for l in range(T):
    i = int(stdin.readline().strip())
    if l == 0 and i == 2:
        arr.append(0)

    if num == 0 or num == i:
        num = i
        cnt+=1
    elif num != i:
        arr.append(cnt)
        num = i
        cnt = 1
else:
    if cnt > 0:
        arr.append(cnt)

dp = [[0]*(W+1) for _ in range(len(arr)+1)]

for i in range(1,len(arr)+1):
    a,b,c = 0,0,0
    for j in range(W+1):
        a,b,c = b,c,0
        c = dp[i-1][j] + (arr[i-1] if (i-1)%2 == j%2 else 0)
        dp[i][j] = max(a,b,c)

print(max(dp[-1]))
