from sys import stdin 

ABCD = sorted(list(map(int,stdin.readline().strip().split())))
print(ABCD[0]*ABCD[2])
