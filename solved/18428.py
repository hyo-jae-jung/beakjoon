from sys import stdin   
from itertools import combinations as comb

N = int(stdin.readline().strip())
hall = [stdin.readline().strip().split() for _ in range(N)]

ans = 'NO'
empty_loc = []
teachers_loc = []
for i in range(N):
    for j in range(N):
        if hall[i][j] == 'T':
            teachers_loc.append((j,i))
        if hall[i][j] == 'X':
            empty_loc.append((j,i))

def surveilance(hall,loc):
    x = loc[0]
    y = loc[1]
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        i = 1
        while 0 <= (nx:=x+dx*i) < N and 0 <= (ny:=y+dy*i) < N:
            if hall[ny][nx] == 'S':
                return True
            if hall[ny][nx] == 'O':
                break
            i+=1
    return False

for three_locs in comb(empty_loc,3):
    for loc in three_locs:
        hall[loc[1]][loc[0]] = 'O'
    for teacher_loc in teachers_loc:
        if surveilance(hall,teacher_loc):
            break
    else:
        ans = 'YES'
        break
    for loc in three_locs:
        hall[loc[1]][loc[0]] = 'X'

print(ans)
