from sys import stdin 

N = int(stdin.readline().strip())
k = int(stdin.readline().strip())

left = 0
right = N**2

while left < right:
    mid = (left+right)//2

    cnt = 0
    for i in range(1,N+1):
        cnt+=min(N, mid//i)

    if cnt < k:
        left = mid + 1
    else:
        right = mid 

print(right)
