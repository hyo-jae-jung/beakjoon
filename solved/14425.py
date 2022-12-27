import sys

N,M = map(int,sys.stdin.readline().strip().split())

N_set = set(sys.stdin.readline().strip() for _ in range(N))

answer = 0
for i in range(M):
    if sys.stdin.readline().strip() in N_set:
        answer+=1

print(answer)

