from sys import stdin  

N,K,P = map(int,stdin.readline().strip().split())
arr = list(map(int,stdin.readline().strip().split()))

ans = 0
while arr:
    tmp = 0
    for _ in range(K):
        tmp+=arr.pop()

    if tmp > K-P:
        ans+=1

print(ans)
