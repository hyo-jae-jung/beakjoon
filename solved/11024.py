from sys import stdin  

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    ans.append(sum(map(int,stdin.readline().strip().split())))

print(*ans,sep='\n')
