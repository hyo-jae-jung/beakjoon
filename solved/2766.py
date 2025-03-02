from sys import stdin  
from collections import deque

def solution(arr):
    n = len(arr)
    arr = deque(map(lambda x:x//2,arr))
    arr2 = arr.copy()
    t = arr2.popleft()
    arr2.append(t)
    s = []
    for i in range(n):
        tt = arr[i] + arr2[i]
        if tt%2 != 0:
            tt+=1
        s.append(tt)

    return s

def check(arr):
    n = len(arr)
    for i in range(n):
        if arr[i%n] != arr[(i-1)%n]:
            return False
    return True

ans = []
while (N:=int(stdin.readline().strip())) > 0:
    arr = []
    for _ in range(N):
        arr.append(int(stdin.readline().strip()))
    i = 0
    while not check(arr):
        arr = solution(arr)
        i+=1
    
    ans.append((i,arr[0]))
    
for i in ans:
    print(*i)
