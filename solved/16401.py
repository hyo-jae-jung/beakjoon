from sys import stdin   

M,N = map(int,stdin.readline().strip().split())
bars = list(map(int,stdin.readline().strip().split()))

left = 0
right = max(bars)

while left < right:

    mid = (left+right)//2 + (1 if (left+right)%2 > 0 else 0)
    cnt = 0
    for i in bars:
        cnt+=i//mid

    if cnt < M:
        right = mid - 1
    else:
        left = mid

print(left)
