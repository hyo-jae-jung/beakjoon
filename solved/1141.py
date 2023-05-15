from sys import stdin 

N = int(stdin.readline().strip())
S = []
for _ in range(N):
    temp = stdin.readline().strip()
    S.append([temp,len(temp)])

S.sort(key=lambda x:-x[1])
answer = 0
S2 = sum(S,[])[::2]
while S2:
    temp=S2.pop()
    for i in S2:
        if i[:len(temp)] == temp:
            break
    else:
        answer+=1

print(answer)
        