from sys import stdin 

N = int(stdin.readline().strip())

arr = []
for _ in range(N):
    arr.append((map(int,stdin.readline().strip().split())))

arr.sort(key=lambda x:x[1])

