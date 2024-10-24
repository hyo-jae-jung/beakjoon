from sys import stdin  

n,m = map(int,stdin.readline().strip().split())
board = []
for _ in range(n):
    tmp = []
    for i in stdin.readline().strip().split():
        tmp.append(i.count('9'))
    board.append(tmp)

max_9 = 0

for i in board:
    max_9 = max(sum(i),max_9)

total_cnt_9 = 0
for i in range(m):
    tmp = 0
    for j in range(n):
        tmp+=board[j][i]
    total_cnt_9+=tmp
    max_9 = max(tmp,max_9)

print(total_cnt_9 - max_9)
