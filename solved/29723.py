from sys import stdin  

N,M,K = map(int,stdin.readline().strip().split())
d = {}
for _ in range(N):
    subject,score = stdin.readline().strip().split()
    d.update({subject:int(score)})

alpha = 0
for _ in range(K):
    alpha+=d.pop(stdin.readline().strip())

rest_score = sorted(d.values())

print(alpha+sum(rest_score[:M-K]),alpha+sum(rest_score[len(rest_score)+K-M:]))
