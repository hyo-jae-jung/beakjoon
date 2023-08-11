from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())
students = deque(map(int,stdin.readline().strip().split()))

turn = 1
buffer = []

while turn <= N:
    if students:
        tmp1 = students.popleft()
        if turn == tmp1:
            turn+=1
            continue
    
    if buffer:
        if turn == buffer[-1]:
            buffer.pop()
            turn+=1
            students.appendleft(tmp1)
            continue
        else:
            if not students:
                print('Sad')
                break
            
    buffer.append(tmp1)
else:
    print('Nice')
    