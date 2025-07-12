def solution(x,y,n):
    x,y = max(x,y),min(x,y)
    if n <= 2:
        return 'YES'
    if x%n == 2 and y%n == 0:
        return 'YES'
    if x%n == 1 and y%n == 1:
        return 'YES'
    if x%n == 0 and y%n == 2:
        return 'YES'
    return 'NO'

from sys import stdin  

X,Y = map(int,stdin.readline().strip().split())
N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    ans.append(solution(X,Y,int(stdin.readline().strip())))

print(*ans,sep='\n')
