from sys import stdin 

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    ans.append(stdin.readline().strip().lower())

print(*ans,sep='\n')

