import sys

N = int(sys.stdin.readline().strip())
points = list(map(int,sys.stdin.readline().strip().split()))

d = dict()
set_points = set(points)
for i in set_points:
    d[i] = sum([1 for j in set_points if i>j])

print(' '.join([str(d[i]) for i in points]))
