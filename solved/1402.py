from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    _ = stdin.readline().strip()
    ans.append('yes')

print(*ans,sep='\n')
