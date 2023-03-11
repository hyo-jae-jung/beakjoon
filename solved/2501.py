from sys import stdin 

N,K = map(int,stdin.readline().strip().split())
aliquot = []
for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        aliquot.append(i)
        if N//i not in aliquot:
            aliquot.append(N//i)

answer = sorted(aliquot)

if len(answer) < K:
    print(0)
else:
    print(answer[K-1])
