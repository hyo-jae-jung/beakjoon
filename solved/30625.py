import sys

N,M = map(int,sys.stdin.readline().strip().split())
dance_type_and_direction = [tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

arr = [[1]+[0]*N]
arr.append([0]*(N+1))

for round in range(1,N+1):
    a,b = 0,0,
    if dance_type_and_direction[round-1][1] == 0:
        a = 1
        b = M-1
    else:
        a = M-1
        b = 1

    arr[0][round] = arr[0][round-1]*a%(10**9+7)
    arr[1][round] = (arr[0][round-1]*b + arr[1][round-1]*a)%(10**9+7)

print((arr[0][-1]+arr[1][-1])%(10**9+7))
