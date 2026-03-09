from sys import stdin 
from heapq import heappop,heappush
from copy import deepcopy

N = int(stdin.readline().strip())
img = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

while N > 1:
    new_img = [[0]*(N//2) for _ in range(N//2)]

    for i in range(0,N,2):
        for j in range(0,N,2):
            tmp = []
            for k in range(2):
                for l in range(2):
                    heappush(tmp,-img[i+k][j+l])
            heappop(tmp)
            val = heappop(tmp)
            new_img[i//2][j//2] = -val

    img = deepcopy(new_img)
    N//=2

print(img[0][0])
