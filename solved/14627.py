from sys import stdin  

S,C = map(int,stdin.readline().strip().split())
L = []
for _ in range(S):
    L.append(int(stdin.readline().strip()))

left = 0
right = max(L)

while left < right:
    mid = (left+right)//2 + (1 if (left+right)%2 > 0 else 0)

    cnt = 0
    for i in L:
        cnt+=i//mid

    if cnt >= C:
        left = mid
    else:
        right = mid - 1
    
print(sum(L) - C*left)
