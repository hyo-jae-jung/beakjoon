from sys import stdin   

ans = []
for _ in range(3):
    N = int(stdin.readline().strip())
    result = 0
    for _ in range(N):
        result+=int(stdin.readline().strip())
    
    if result > 0:
        ans.append('+')
    elif result < 0:
        ans.append('-')
    else:
        ans.append('0')

print(*ans,sep='\n')
