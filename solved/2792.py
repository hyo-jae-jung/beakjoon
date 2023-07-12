from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
jewels = []
for _ in range(M):
    jewels.append(int(stdin.readline().strip()))

left = 1
right = max(jewels)
answer = 0
while left<=right:
    mid = (left+right)//2
    terms = sum(i//mid + (1 if i%mid else 0) for i in jewels)

    if terms > N:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
