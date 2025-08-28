from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
ans = [-1]*N
i = 0
for j in range(1,N):
    if A[i] != A[j]:
        for k in range(i,j):
            ans[k] = j+1
        i = j
    
print(*ans)
