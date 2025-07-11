from sys import stdin   

T = int(stdin.readline().strip())
ans = []
stage = [[0]*11 for _ in range(11)]
stage[0][1] = 1

for i in range(1,11):
    for j in range(1,11):
        stage[i][j] = stage[i-1][j] + stage[i][j-1]

for i in range(1,T+1):
    r,c = map(int,stdin.readline().strip().split())
    ans.append(f"Case #{i}: {stage[r][c]}")

print(*ans,sep='\n')
