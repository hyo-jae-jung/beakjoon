from sys import stdin

N = int(stdin.readline().strip())

memo = [[0]+[1]*9]

for _ in range(N-1):
    memo.append([0]*10)

if N > 1:
    memo[0][0] = 1

for i in range(1,N):
    for j in range(10):
        if j-1>=0:
            memo[i][j]+=memo[i-1][j-1]
        if j+1<=9:
            memo[i][j]+=memo[i-1][j+1]
else:
    memo[-1][0] = 0

print(sum(memo[-1])%(10**9))
