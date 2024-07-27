from sys import stdin  

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))

arr.sort()

ans = 0
tmp = arr[0]
for i in range(1,N):
    if arr[i] != arr[i-1] + 1:
        ans+=tmp
        tmp = arr[i]
else:
    ans+=tmp
    
print(ans)
