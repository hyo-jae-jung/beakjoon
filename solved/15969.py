from sys import stdin 

_ = stdin.readline()
scores = list(map(int,stdin.readline().strip().split()))

print(max(scores)-min(scores))
