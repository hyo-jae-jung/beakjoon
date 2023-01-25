from sys import stdin 
import re

N = int(stdin.readline().strip())

answer = []
p = re.compile('^[0-9a-zA-Z]{6,9}$')

for _ in range(N):
    if p.match(stdin.readline().strip()):
        answer.append('yes')
    else:
        answer.append('no')

print(*answer,sep='\n')
