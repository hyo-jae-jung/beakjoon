from sys import stdin  

N,M,L = map(int,stdin.readline().strip().split())
if N > 0:
    I = sorted(list(map(int,stdin.readline().strip().split())))
else:
    I = []
H = [0] + I + [L]
left = 1
right = 0
D = []
for i in range(1,N+2):
    D.append(H[i] - H[i-1])
    right = max(right,D[-1])

while left < right:

    mid = (left+right)//2
    cnt = 0
    for i in D:
        if mid < i:
            cnt+=(i-mid)//mid + (1 if i%mid > 0 else 0)

    if cnt > M:
        left = mid + 1
    else:
        right = mid

print(right)
