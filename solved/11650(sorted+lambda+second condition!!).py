import sys

N = int(sys.stdin.readline().strip())
points = [tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
for i,j in sorted(points,key=lambda x:(x[0],x[1])):
    print("{} {}".format(i,j))
