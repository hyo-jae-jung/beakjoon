from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
h = max(map(int,stdin.readline().strip().split()))
a = max(map(int,stdin.readline().strip().split()))
print(h+a)
