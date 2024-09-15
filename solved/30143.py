from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N,A,D = map(int,stdin.readline().strip().split())
    ans.append(N*(2*A+(N-1)*D)//2)

print(*ans,sep='\n')
