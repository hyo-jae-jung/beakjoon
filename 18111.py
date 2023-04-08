from sys import stdin 

N,M,B = map(int,stdin.readline().strip().split())

earth_met = []
for _ in range(N):
    earth_met.append(list(map(int,stdin.readline().strip().split())))

earth_arr = sum(earth_met,[])
    
right = (sum(earth_arr)+B)//(N*M)
left = 0

while left <= right:
    mid = (right+left)//2
    left_time = sum((i-left)*2 if i>left else (left-i) for i in earth_arr)
    mid_time = sum((i-mid)*2 if i>mid else (mid-i) for i in earth_arr)
    right_time = sum((i-right)*2 if i>right else (right-i) for i in earth_arr)

    if abs(left_time - mid_time) > abs(right_time - mid_time):
        left = mid + 1
    elif abs(left_time - mid_time) < abs(right_time - mid_time):
        right = mid - 1
    else:
        left = (left+mid)//2
        right = (mid+right)//2

print(mid_time,mid)
