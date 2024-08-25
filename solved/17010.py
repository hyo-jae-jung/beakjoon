from sys import stdin  

L = int(stdin.readline().strip())
ans = []
for _ in range(L):
    N,x = stdin.readline().strip().split()
    ans.append(int(N)*x)

print(*ans,sep='\n')
