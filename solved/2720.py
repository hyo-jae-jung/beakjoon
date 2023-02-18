from sys import stdin 

T = int(stdin.readline().strip())

answer = []
for _ in range(T):
    Q,D,N,P = 0,0,0,0
    C = int(stdin.readline().strip())
    while C >= 25:
        C-=25
        Q+=1
    while C >= 10:
        C-=10
        D+=1
    while C >= 5:
        C-=5
        N+=1
    while C >= 1:
        C-=1
        P+=1
    answer.append([Q,D,N,P])

for i in answer:
    print(*i)
