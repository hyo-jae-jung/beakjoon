from sys import stdin 

N = int(stdin.readline().strip())
scores = list(map(int,stdin.readline().strip().split()))

c = []
i = 0
cnt = 0
while i < N:
    if scores[i] == 1:
        cnt+=1
    else:
        if cnt:
            c.append(cnt)
            cnt = 0
    i+=1
else:
    if cnt:
        c.append(cnt)

answer = 0
for i in c:
    answer+=i*(i+1)//2

print(answer)
