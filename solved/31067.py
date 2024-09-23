from sys import stdin 

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))
ans = 0
i = 0
while i < len(A)-1:
    if A[i] >= A[i+1]:
        A[i+1]+=K
        ans+=1

    if A[i] >= A[i+1]:
        ans = -1
        break

    i+=1

print(ans)
