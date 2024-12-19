from sys import stdin  

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
rooms = [1]*(N+1)

for _ in range(M):
    x,y = map(int,stdin.readline().strip().split())
    for i in range(x,y):
        rooms[i] = 0

print(sum(rooms)-1)
