from sys import stdin

N = int(stdin.readline().strip())
P = int(stdin.readline().strip())
for _ in range(N-1):
    temp = int(stdin.readline().strip())
    diff = temp-P
    