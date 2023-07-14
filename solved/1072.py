from sys import stdin 

X,Y = map(int,stdin.readline().strip().split())

left = 1
right = 10**9
criterion  = int(100*Y/X)+1
answer = -1
while left <= right:
    mid = (left+right)//2
    if int(100*((Y+mid)/(X+mid))) >= criterion:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
        
print(answer)
