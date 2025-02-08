from sys import stdin   

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N,C = map(int,stdin.readline().strip().split())
    ans.append(N//C+(1 if N%C else 0))

print(*ans,sep='\n')
