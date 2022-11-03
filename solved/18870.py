import sys

N = int(sys.stdin.readline().strip())
points = list(map(int,sys.stdin.readline().strip().split()))

d = dict()
set_points = sorted(set(points))
for i,j in enumerate(set_points):
    d[j] = i

print(' '.join([str(d[i]) for i in points]))
