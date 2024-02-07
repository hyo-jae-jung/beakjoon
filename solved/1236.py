from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
row_gard = [True]*M
col_gard = [True]*N
gards = []

for i in range(N):
    for j,k in enumerate(stdin.readline().strip()):
        if k == 'X':
            row_gard[j] = False
            col_gard[i] = False

print(max(sum(row_gard),sum(col_gard)))
