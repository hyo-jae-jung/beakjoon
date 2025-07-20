from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
table = [list(stdin.readline().strip()) for _ in range(N)]

max_square_number = -1

def check_square_number(n):
    if (a:=int(n**0.5))*a == n:
        return n
    return -1

for x in range(M):
    for y in range(N):
        for xd in range(-M,M,1):
            for yd in range(-N,N,1):
                tmp = ''
                for k in range(max(N,M)):
                    if all([xd==0,yd==0]):
                        tmp+=table[y][x]
                        break
                    if 0 <= x+xd*k < M and 0 <= y+yd*k < N:
                        tmp+=table[y+yd*k][x+xd*k]

                    max_square_number = max(max_square_number,check_square_number(int(tmp)))

print(max_square_number)
