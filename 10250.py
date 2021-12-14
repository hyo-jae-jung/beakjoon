T = int(input())
data = []
rooms = []
for i in range(T):
    data.append(input())
for i in data:
    H,W,N = map(int,i.split())
    if N%H == 0:
        YY = H
        XX = N//H
    else:
        YY = N%H
        XX = N//H + 1

    XX = str(XX).zfill(2)

    YYXX = str(YY)+XX
    rooms.append(YYXX)

for i in rooms:
    print(i)