from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
DNAs = []
for _ in range(N):
    DNAs.append(stdin.readline().strip())

answer = ''
for i in range(M):
    newc = {
    'A':0,
    'C':0,
    'G':0,
    'T':0,
    }
    for j in range(N):
        newc[DNAs[j][i]]+=1
    answer+=sorted(newc.items(),key=lambda x:(-x[1],x[0]))[0][0]

cnt = 0
for i in DNAs:
    for j in range(M):
        if i[j] != answer[j]:
            cnt+=1

print(answer,cnt,sep='\n')
