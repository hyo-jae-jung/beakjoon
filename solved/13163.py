from sys import stdin  

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    S = stdin.readline().strip().split()
    tmp = 'god'
    for i in range(1,len(S)):
        tmp+=S[i]
    ans.append(tmp)

print(*ans,sep='\n')
