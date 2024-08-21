from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    l = sorted(list(map(int,stdin.readline().strip().split())))
    ans.append(str(l[0]) + ' ' + str(l[-1]))

print(*ans,sep='\n')
