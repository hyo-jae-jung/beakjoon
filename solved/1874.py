N = int(input())
M = [int(input()) for _ in range(N)]

plus_minus = []
temp = []
answer = []
i=0
j=0
while len(answer)<N:
    plus_minus.append('+')
    temp.append(i+1)
    if temp[-1]>M[j]:
        break
    while temp and j<N:
        if temp[-1]==M[j]:
            answer.append(temp.pop())
            plus_minus.append('-')
            j+=1
        else:
            break
    i+=1

if answer==M:
    [print(i) for i in plus_minus]
else:
    print('NO')
