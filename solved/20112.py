from sys import stdin  

N = int(stdin.readline().strip())
ism = []
for _ in range(N):
    ism.append(list(stdin.readline().strip()))

ans = 'YES'

for i in range(N):
    for j in range(i,N):
        if ism[i][j] != ism[j][i]:
            ans = 'NO'
            break

print(ans)
