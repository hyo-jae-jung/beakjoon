from sys import stdin 
from collections import defaultdict

T = int(stdin.readline().strip())
answer = []

def disassemble(n):
    div = 2
    d = defaultdict(int)
    while n != 1:
        if n%div == 0:
            d[div]+=1
            n = n//div
        else:
            div+=1
    return d

for _ in range(T):
    answer.append(disassemble(int(stdin.readline().strip())))
    
for i in answer:
    for j,k in i.items():
        print(j,k)
