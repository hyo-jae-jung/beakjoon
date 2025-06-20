from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
rectangle = [list(stdin.readline().strip()) for _ in range(N)]

min_x,min_y = M,N
max_x,max_y = -1,-1
for i in range(N):
    for j in range(M):
        if rectangle[i][j] == '#':
            min_x = min(min_x,j)
            max_x = max(max_x,j)
            min_y = min(min_y,i)
            max_y = max(max_y,i)

m = (max_x - min_x)//2

if rectangle[min_y][min_x+m] == ".":print("UP")
elif rectangle[min_y+m][min_x] == ".":print("LEFT")
elif rectangle[max_y][max_x-m] == ".":print("DOWN")
elif rectangle[max_y-m][max_x] == ".":print("RIGHT")
