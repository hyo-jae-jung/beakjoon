from sys import stdin  
from collections import deque 

Buffer = deque()
N = int(stdin.readline().strip())
while (packet:=int(stdin.readline().strip())) != -1:
    if packet == 0:
        Buffer.popleft()
    else:
        if len(Buffer) < N:
            Buffer.append(packet)

if not Buffer:
    Buffer.append('empty')
    
print(*Buffer)
