from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
arr = [0]*M
for _ in range(N):
    row = list(map(int,stdin.readline().strip().split()))
    for i in range(M):
        arr[i]+=row[i]

A = int(stdin.readline().strip())
B = [0]
for i in range(M):
    B.append(B[-1]+arr[i])

ans = 0
for j in range(A,M+1):
    ans = max(ans,B[j]-B[j-A])

print(ans)
