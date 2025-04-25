from sys import stdin  

N = int(stdin.readline().strip())
ans = []
a,b = 0,0
for _ in range(N):
    A,B = map(int,stdin.readline().strip().split())
    a+=A
    b+=B
    ans.append(a-b)

print(*ans,sep='\n')
