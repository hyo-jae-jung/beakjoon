from sys import stdin   

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
ans = [0]
i,j = 0,1
m = A[i]

while j < N:
    while i <= j:
        m = min(m,A[i])
        i+=1
    if ans[-1] < A[j] - m:
        ans.append(A[j] - m)
    else:
        ans.append(ans[-1])
    j+=1

print(*ans)
