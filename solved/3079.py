from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
T = []
for _ in range(N):
    T.append(int(stdin.readline().strip()))

left = 0
right = M*max(T)

while left < right:

    mid = (left+right)//2

    cnt = 0
    for i in T:
        cnt+=mid//i

    if cnt >= M:
        right = mid
    else:
        left = mid + 1

print(left)
