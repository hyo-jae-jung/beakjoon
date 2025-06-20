from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
rectangle = [list(stdin.readline().strip()) for _ in range(N)]

def solution():
    for square in range(min(N,M)-1,-1,-1):
        for i in range(square,N):
            for j in range(square,M):
                if rectangle[i][j] == rectangle[i-square][j] == rectangle[i][j-square] == rectangle[i-square][j-square]:
                    return (square+1)**2

print(solution())
