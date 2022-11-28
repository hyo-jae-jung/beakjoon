import sys

A_cnt, B_cnt = map(int,sys.stdin.readline().strip().split())
A = set(map(int,sys.stdin.readline().strip().split()))
B = set(map(int,sys.stdin.readline().strip().split()))

print(len(A-B)+len(B-A))
