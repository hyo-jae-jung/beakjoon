from sys import stdin  

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
lamp_loc = list(map(int,stdin.readline().strip().split()))

left = 1
right = N

while left < right:
    mid = (left+right)//2
    if lamp_loc[0] - mid > 0:
        left = mid + 1
        continue

    if lamp_loc[-1] + mid < N:
        left = mid + 1
        continue

    check = True
    for i in range(len(lamp_loc)-1):
        if lamp_loc[i] + mid < lamp_loc[i+1] - mid:
            left = mid + 1
            check = False
            break
    if check:
        right = mid

print(right)
