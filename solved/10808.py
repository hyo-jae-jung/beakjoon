import sys

S = sys.stdin.readline().strip()

d = {}
for i in range(26):
    d[chr(97+i)]=0

for i in S:
    d[i]+=1

print(*d.values())
