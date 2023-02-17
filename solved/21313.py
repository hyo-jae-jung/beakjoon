from sys import stdin 

N = int(stdin.readline().strip())
answer = []
for i in range(N-1):
    if i%2 == 0:
        answer.append(1)
    else:
        answer.append(2)
else:
    if i%2==0:
        answer.append(2)
    else:
        answer.append(3)

print(*answer)
