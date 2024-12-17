from sys import stdin  
from collections import deque

n = int(stdin.readline().strip())
gravel = deque(map(int,stdin.readline().strip().split()))

left,right = [],[]

while gravel:
    if sum(left) <= sum(right):
        left.append(gravel.popleft())
    else:
        right.append(gravel.popleft())

ans = 0

diff = abs(sum(left) - sum(right))

def divide(a,b):
    return a//b,a%b

for i in [100,50,20,10,5,2,1]:
    val,rest = divide(diff,i)
    ans+=val
    diff = rest

print(ans)
