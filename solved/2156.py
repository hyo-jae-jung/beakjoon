import sys

n = int(sys.stdin.readline().strip())
wines = []
for _ in range(n):
    wines.append(int(sys.stdin.readline().strip()))

memo = []
for _ in range(n):
    memo.append([0]*3)

memo[0][1] = wines[0]

for i in range(1,n):
    for j in range(3):
        if j == 2:
            memo[i][0] = max(memo[i-1])
        else:
            memo[i][j+1] = memo[i-1][j] + wines[i]

print(max(memo[-1]))
