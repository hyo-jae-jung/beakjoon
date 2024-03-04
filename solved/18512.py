from sys import stdin 

X,Y,P1,P2 = map(int,stdin.readline().strip().split())
cnt = 0
while P1 != P2:
    if P1 > P2:
        P2+=Y
    elif P1 < P2:
        P1+=X        
    if cnt > 1000:
        print(-1)
        break
    cnt+=1
else:
    print(P1)
