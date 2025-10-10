from sys import stdin 

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())

snail = [[0]*N for _ in range(N)]
snail[N//2][N//2] = 1
def cycle(x,y,n,arr,d=1):

    if d > N//2:
        return True

    y-=1
    n+=1
    arr[y][x] = n

    for i in range(2*d-1):
        x+=1
        n+=1
        arr[y][x] = n

    for i in range(2*d):
        y+=1
        n+=1
        arr[y][x] = n

    for i in range(2*d):
        x-=1
        n+=1
        arr[y][x] = n

    for i in range(2*d):
        y-=1
        n+=1
        arr[y][x] = n

    return cycle(x,y,n,arr,d+1)

cycle(N//2,N//2,1,snail,1)

for i in snail:
    print(*i)

for i in range(N):
    for j in range(N):
        if snail[i][j] == M:
            print(i+1,j+1)
            break
