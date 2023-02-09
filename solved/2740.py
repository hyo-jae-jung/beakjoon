from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
A = []
for _ in range(N):
    A.append(list(map(int,stdin.readline().strip().split())))

M,K = [int(i) for i in stdin.readline().strip().split()]
B = []
for _ in range(M):
    B.append(list(map(int,stdin.readline().strip().split())))

answer = []

for i in A:
    temp = []
    for j in range(K):
        temp.append(sum([i*j for i,j in zip(i,sum(B,[])[j::K])]))
    answer.append(temp)

for i in answer:
    print(*i)
