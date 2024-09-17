from sys import stdin  

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    tmp = stdin.readline().strip()
    if tmp[-1] == '.':
        ans.append(tmp)
    else:
        ans.append(tmp+'.')

print(*ans,sep='\n')
