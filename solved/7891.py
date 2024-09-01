from sys import stdin  

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    x,y = map(int,stdin.readline().strip().split())
    ans.append(x+y)

print(*ans,sep='\n')
