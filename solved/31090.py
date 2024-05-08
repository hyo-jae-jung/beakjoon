from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    ans.append('Good' if (N+1)%int(str(N)[-2:]) == 0 else 'Bye')

print(*ans,sep='\n')
