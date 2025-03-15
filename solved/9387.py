from sys import stdin   

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    m,n = map(int,stdin.readline().strip().split())
    tiles = list(map(int,stdin.readline().strip().split()))

    if 2 in tiles:
        direction = True
    else:
        direction = False

    if direction:
        i = tiles.index(2)
    else:
        i = tiles.index(3)

    tiles[i] = 1
    y = 0
    while n:
        if direction:
            if i+1 < m:
                i+=1
            else:
                direction = False
                i-=1
        else:
            if i > 0:
                i-=1
            else:
                direction = True
                i+=1
        if tiles[i] == 0:
            y+=1
        n-=1

    ans.append(y)

print(*ans,sep='\n')
