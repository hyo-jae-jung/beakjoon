from sys import stdin 
from collections import deque

n = int(stdin.readline().strip())

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    arr = deque([0,1])
    
    i=2
    while i <= n:
        num = arr[0] + arr[1]
        arr.append(num)
        arr.popleft()
        i+=1
    return arr[-1]

print(fibonacci(n))
