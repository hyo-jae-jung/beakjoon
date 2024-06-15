from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    tmp = []
    n = int(stdin.readline().strip())
    for _ in range(n//5):
        tmp.append('++++')
    
    tmp.append('|'*(n%5))

    ans.append(' '.join(tmp))

print(*ans,sep='\n')
