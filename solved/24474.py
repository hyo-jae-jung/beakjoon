from sys import stdin 
from collections import deque

X = deque()
def make_odd(n):
    i = 1
    while n%2 == 0:
        n = n//2
        i*=2
    return (n,i)

N = int(stdin.readline().strip())
for _ in range(N):
    A = int(stdin.readline().strip())
    X.append(make_odd(A))

def solution(x):
    global X
    while x > 0:
        val,num = X.popleft()
        if num >= x:
            num-=x
            x = 0
            result = val
            if num > 0:
                X.appendleft((val,num))
        elif num < x:
            x-=num
    return result
            
p = 0
ans = []
Q = int(stdin.readline().strip())
for _ in range(Q):
    x = int(stdin.readline().strip())
    ans.append(solution(x-p) if x > p else ans[-1])
    p = x

print(*ans,sep='\n')
