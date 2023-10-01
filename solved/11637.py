from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    n = int(stdin.readline().strip())
    arr = []
    total_cnt=0
    for i in range(1,n+1):
        cnt = int(stdin.readline().strip())
        arr.append((i,cnt))
        total_cnt+=cnt
    arr.sort(key=lambda x:x[1])
    if arr[-2][1] == arr[-1][1]:
        answer.append("no winner")
    else:
        answer.append(("majority" if (2*arr[-1][1] > total_cnt) else "minority")+ f" winner {arr[-1][0]}")

print(*answer,sep='\n')
