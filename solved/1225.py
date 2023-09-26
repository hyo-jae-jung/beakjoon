from sys import stdin

A,B = map(str,stdin.readline().strip().split())

print(sum(int(i)*int(j) for i in A for j in B))
