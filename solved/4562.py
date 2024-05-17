from sys import stdin  

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    X,Y = map(int,stdin.readline().strip().split())
    if X >= Y:
        ans.append('MMM BRAINS')
    else:
        ans.append('NO BRAINS')

print(*ans,sep='\n')
