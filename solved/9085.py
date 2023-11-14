from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    _ = stdin.readline().strip()
    ans.append(sum(map(int,stdin.readline().strip().split())))

print(*ans,sep='\n')
