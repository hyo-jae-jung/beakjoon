import sys

N = int(sys.stdin.readline().strip())
A = map(int,sys.stdin.readline().strip().split())
M_cnt = int(sys.stdin.readline().strip())
M = map(int,sys.stdin.readline().strip().split())

for i in M:
    if i in A:
        print(1)
    else:
        print(0)
