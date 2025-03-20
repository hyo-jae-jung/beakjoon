from sys import stdin   

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n = int(stdin.readline().strip())
    ans.append(int(n*(n+1)*(2*n+1)/12 + n*(n+1)/4))

print(*ans,sep='\n')
