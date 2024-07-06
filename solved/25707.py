from sys import stdin  

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))
arr.sort()
ans = 0
for i in range(N):
    ans+=abs(arr[i%N]-arr[(i-1)%N])

print(ans)
