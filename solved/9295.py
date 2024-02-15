from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for i in range(1,T+1):
    ans.append(f'Case {i}: {sum(map(int,stdin.readline().strip().split()))}')

print(*ans,sep='\n')
