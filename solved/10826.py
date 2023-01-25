from sys import stdin 
from collections import deque 

n = int(stdin.readline().strip())

def fibonacci(n:int)->int:

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    arr = deque([0,1])

    for _ in range(2,n+1):
        num = arr[0]+arr[1]
        arr.append(num)
        arr.popleft()

    return arr[-1]

print(fibonacci(n))
