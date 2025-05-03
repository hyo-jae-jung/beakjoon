from sys import stdin 

T = int(stdin.readline().strip())
ns = [int(stdin.readline().strip()) for _ in range(T)]

dp = [[0,0,0] for _ in range(100001)]

dp[1][0] = 1
dp[2][1] = 1
dp[3][2] = 1

for i in range(100000):
    for j in range(3):
        for k in [-1,1]:
            if i+(j+k)%3+1 <= 100000:
                dp[i+(j+k)%3+1][(j+k)%3]+=dp[i][j]%1000000009

ans = []
for i in ns:
    ans.append(sum(dp[i])%1000000009)

print(*ans,sep='\n')
