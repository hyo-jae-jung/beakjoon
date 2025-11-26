from sys import stdin  

n = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
m = int(stdin.readline().strip())
B = list(map(int,stdin.readline().strip().split()))

ans = []
for i in range((m-n)//(n-1)+1):
    for j in range(0,m-n+1-i*(n-1)):
        for k in range(n):
            if A[k] != B[j+k*(i+1)]:
                break
        else:
            ans.append(i)

if ans:
    ans.sort()
    print(ans[0],ans[-1])
else:
    print(-1)
