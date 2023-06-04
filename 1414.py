from sys import stdin 

N = int(stdin.readline().strip())
d = dict()
for i in range(1,27):
    d[chr(96+i)] = i

for i in range(27,53):
    d[chr(38+i)]=i

