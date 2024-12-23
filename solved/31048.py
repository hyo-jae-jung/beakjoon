from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    tmp = 1
    for i in range(2,int(stdin.readline().strip())+1):
        tmp*=i
    ans.append(str(tmp)[-1])

print(*ans,sep='\n')
