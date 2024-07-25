from sys import stdin  

T = int(stdin.readline().strip())

ans = []
for _ in range(T):
    tmp = stdin.readline().strip()
    if len(tmp)%2 == 1:
        tmp+=tmp
    ans.append(''.join(tmp[0::2]))
    ans.append(''.join(tmp[1::2]))

print(*ans,sep='\n')
