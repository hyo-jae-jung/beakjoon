from sys import stdin 

K,N = map(int,stdin.readline().strip().split())
lines_k = []
for _ in range(K):
    lines_k.append(int(stdin.readline().strip()))

right = sum(lines_k)//N
left = 1
mid = (right + left)//2

while left <= right:
    temp = sum(i//mid for i in lines_k)
    if temp >= N:
        left = mid + 1
    elif temp < N:
        right = mid - 1
    mid = (right + left)//2

print(mid)
