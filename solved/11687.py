from sys import stdin  

M = int(stdin.readline().strip())

def solution(y):
    i = 0
    ans = 0
    while 5**i <= y:
        ans+=y//(5**i)
        i+=1
    return ans

left = 1
right = 10**8

while left < right:
    mid = (left+right)//2
    x = solution(mid)
    
    if x >= M:
        right = mid
    else:
        left = mid + 1
else:
    if solution(right) == M:
        print(right*5)
    else:
        print(-1)
