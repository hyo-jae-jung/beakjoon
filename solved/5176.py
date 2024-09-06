from sys import stdin  

K = int(stdin.readline().strip())
ans = []
for _ in range(K):
    P,M = map(int,stdin.readline().strip().split())
    sitting = [0]*(M+1)
    cnt = 0
    for _ in range(P):
        p = int(stdin.readline().strip())
        if sitting[p]:
            cnt+=1
        else:
            sitting[p] = 1
    ans.append(cnt)

print(*ans,sep='\n')
