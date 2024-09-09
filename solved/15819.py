from sys import stdin  

N,I = map(int,stdin.readline().strip().split())
handle = []
for _ in range(N):
    handle.append(stdin.readline().strip())

handle.sort()

print(handle[I-1])
