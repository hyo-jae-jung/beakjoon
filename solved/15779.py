from sys import stdin   

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
d = []
d.append(A[0])

ans = 1
for i in range(1,N):

    if len(d) == 1:
        d.append(A[i])
        continue

    if (d[-1] - d[-2])*(d[-1] - A[i]) > 0:
        d.append(A[i])
    else:
        ans = max(ans,len(d))
        d = [d[-1],A[i]]

else:
    ans = max(ans,len(d))
    
print(ans)
