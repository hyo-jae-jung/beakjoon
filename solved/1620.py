import sys

N,M = map(int,sys.stdin.readline().strip().split())
pocketmons = {str(i):sys.stdin.readline().strip() for i,_ in enumerate(range(N),1)}

pocketmons_rev = {j:i for i,j in pocketmons.items()}

pocketmons.update(pocketmons_rev)

answer = []

for i in range(M):
    answer.append(pocketmons[sys.stdin.readline().strip()])

for i in answer:
    print(i)
