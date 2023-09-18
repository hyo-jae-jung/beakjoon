from sys import stdin 

N = int(stdin.readline().strip())
map = []
for _ in range(N):
    map.append(list(stdin.readline().strip()))

answer = [[0]*N for _ in range(N)]

for j in range(N):
    for i in range(N):
        try:
            n = int(map[j][i])
            for dx,dy in [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]:
                nx,ny = i+dx,j+dy
                if 0 <= nx < N and 0 <= ny < N:
                    if isinstance(answer[ny][nx],int):
                        answer[ny][nx]+=n
                        if answer[ny][nx] >= 10:
                            answer[ny][nx] = 'M'
                        
            answer[j][i]='*'
        except:
            pass

for i in answer:
    tmp = ''
    for j in i:
        tmp+=str(j)
    print(tmp)
