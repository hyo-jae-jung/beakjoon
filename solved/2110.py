from sys import stdin   

N,C = map(int,stdin.readline().strip().split())
house = []
for _ in range(N):
    house.append(int(stdin.readline().strip()))

house.sort()

left = 1
right = house[-1]

while left < right:
    mid = (left+right)//2 + (1 if (left+right)%2 > 0 else 0)
    cnt = 1
    i,j = 0,1
    while i+j < N:
        t = house[i+j] - house[i]
        if t >= mid:
            cnt+=1
            i+=j
            j = 1
        else:
            j+=1
    else:
        if i < N-1:
            t = house[-1] - house[i]
            if t >= mid:
                cnt+=1

    if cnt >= C:
        left = mid
    else:
        right = mid - 1

print(right)
