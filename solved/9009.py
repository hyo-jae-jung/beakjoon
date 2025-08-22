from sys import stdin  
from bisect import bisect_left
from collections import deque 

T = int(stdin.readline().strip())
fibo_val = [0,1]
def fibonacci(n):
    while fibo_val[-1] < n:
        fibo_val.append(fibo_val[-1]+fibo_val[-2])
ans = []

for _ in range(T):
    n = int(stdin.readline().strip())
    fibonacci(n)
    tmp = deque()
    while n > 0:
        i = bisect_left(fibo_val,n)
        if fibo_val[i] > n:
            i-=1
        tmp.appendleft(fibo_val[i])
        n-=fibo_val[i]

    ans.append(tmp)

for i in ans:
    print(*i)
