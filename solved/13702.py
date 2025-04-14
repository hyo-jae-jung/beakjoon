from sys import stdin   

N,K = map(int,stdin.readline().strip().split())
bottle = []
for _ in range(N):
    bottle.append(int(stdin.readline().strip()))

left = 0
right = max(bottle)

while left < right:

    mid = (left+right)//2 + (1 if (left+right)%2 > 0 else 0)

    cnt = 0    
    for i in bottle:
        cnt+=i//mid

    if cnt < K:
        right = mid - 1
    else:
        left = mid
    
print(left)
