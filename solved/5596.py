from sys import stdin 

minkook = sum(map(int,stdin.readline().strip().split()))
mansae = sum(map(int,stdin.readline().strip().split()))
print(max(minkook,mansae))
