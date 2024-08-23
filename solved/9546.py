from sys import stdin  

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    ans.append(2**int(stdin.readline().strip())-1)

print(*ans,sep='\n')
