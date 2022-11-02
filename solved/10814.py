import sys

N = int(sys.stdin.readline().strip())
db = [(i,*(lambda x:(int(x[0]),x[1]))(sys.stdin.readline().strip().split())) for i in range(N)]
for _,j,k in sorted(db,key=lambda x:(x[1],x[0])):
    print('{} {}'.format(j,k))
