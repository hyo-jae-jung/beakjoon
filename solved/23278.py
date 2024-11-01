from sys import stdin  

N,L,H = map(int,stdin.readline().strip().split())
scores = list(map(int,stdin.readline().strip().split()))

scores.sort()

print(sum(scores[L:-1*H if H > 0 else None])/(N-L-H))
