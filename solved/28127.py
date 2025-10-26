def solution(a,d,n):
    return a*n - d*n + d*n*(n+1)//2

from sys import stdin  

Q = int(stdin.readline().strip())
ans = []
for _ in range(Q):
    a,d,x = map(int,stdin.readline().strip().split())

    n = 0
    while solution(a,d,n+1) < x:
        n+=1
    
    ans.append((n+1,x-solution(a,d,n)))

for i in ans:
    print(*i)
