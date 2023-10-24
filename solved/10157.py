from sys import stdin 

C,R = map(int,stdin.readline().strip().split())
K = int(stdin.readline().strip())
if C*R < K:
    print(0)
else:
    def border(rest_x,rest_y,rest_k):

        x,y = 1,1
        while rest_k:
            if x == 1 and y == 1:
                dx,dy = 0,1
            elif x == rest_x and y == rest_y:
                dx,dy = 0,-1
            elif x == 1 and y == rest_y:
                dx,dy = 1,0
            elif x == rest_x and y == 1:
                dx,dy = -1,0

            x+=dx
            y+=dy
            rest_k-=1

        global i
        return x+i,y+i

    i = 0
    while (C-2)*2 + R*2 < K:
        K-=(C-2)*2 + R*2
        C-=2
        R-=2
        i+=1

    print(*border(C,R,K-1))
