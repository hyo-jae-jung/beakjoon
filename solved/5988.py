from sys import stdin 

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    if int(stdin.readline().strip()) % 2 == 0:
        ans.append('even')
    else:
        ans.append('odd')

print(*ans,sep='\n')
