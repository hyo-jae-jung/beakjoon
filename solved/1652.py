from sys import stdin  

N = int(stdin.readline().strip())
room = [list(stdin.readline().strip()) for _ in range(N)]

row = 0
for i in room:
    t = 0
    for j in i:
        if j == '.':
            t+=1
        elif j == 'X':
            if t >= 2:
                row+=1
            t = 0
    else:
        if t >= 2:
            row+=1

col = 0
for i in range(N):
    t = 0
    for j in range(N):
        if room[j][i] == '.':
            t+=1
        elif room[j][i] == 'X':
            if t >= 2:
                col+=1
            t = 0
    else:
        if t >= 2:
            col+=1

print(row,col)
