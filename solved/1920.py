import sys

N = int(sys.stdin.readline().strip())
A = map(int,sys.stdin.readline().strip().split())
M_cnt = int(sys.stdin.readline().strip())
M = [int(i) for i in sys.stdin.readline().strip().split()]

d1 = dict.fromkeys(M,0)
d2 = dict.fromkeys(A,1)

d1.update(d2)

for i in M:
    print(d1[i])
