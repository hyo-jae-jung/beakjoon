from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    s,p = stdin.readline().strip().split()
    ans.append(len(s.replace(p,'1')))

print(*ans,sep='\n')
