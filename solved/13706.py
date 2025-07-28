from sys import stdin 
N = int(stdin.readline().strip())

left = 1
right = 10**400

while left < right:
    mid = (left+right)//2
    if mid**2 >= N:
        right = mid
    else:
        left = mid + 1
	
print(right)
