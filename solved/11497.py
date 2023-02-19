from sys import stdin 
from collections import deque 

def logs(arr:list):
    arr.sort()
    arr = deque(arr)
    temp = deque()
    while arr:
        if len(arr)%2 == 0:
            temp.append(arr.pop())
        else:
            temp.appendleft(arr.pop())

    diff = []
    for i in range(len(temp)-1):
        diff.append(abs(temp[i]-temp[i+1]))

    return max(diff)

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    N = int(stdin.readline().strip())
    L = [int(i) for i in stdin.readline().strip().split()]
    answer.append(logs(L))

print(*answer, sep='\n')
