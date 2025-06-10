from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n,m = map(int,stdin.readline().strip().split())
    cnt = 0
    for i in range(1,n):
        for j in range(1,i):
            if (i**2 + j**2 + m)%(i*j) == 0:
                cnt+=1
    ans.append(cnt)

print(*ans,sep='\n')
