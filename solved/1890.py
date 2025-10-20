from sys import stdin   

N = int(stdin.readline().strip())
board = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] > 0 and board[i][j] > 0:
            if j+board[i][j] < N:
                dp[i][j+board[i][j]]+=dp[i][j]
            if i+board[i][j] < N:
                dp[i+board[i][j]][j]+=dp[i][j]

print(dp[-1][-1])
