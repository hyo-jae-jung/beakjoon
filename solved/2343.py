from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
lecture = list(map(int,stdin.readline().strip().split()))

left = max(lecture)
right = sum(lecture)

while left < right:
    mid = (left+right)//2
    blueray_cnt = 0
    blueray_val = 0
    blueray = []
    for i in lecture:
        if blueray_val+i <= mid:
            blueray_val+=i
        else:
            blueray_cnt+=1
            blueray_val = i
    else:
        blueray_cnt+=1
    
    if blueray_cnt <= M:
        right = mid
    else:
        left = mid + 1

print(right)
