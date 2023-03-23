from sys import stdin 
from collections import defaultdict

S = stdin.readline().strip()
q = int(stdin.readline().strip())
d = defaultdict(list)

def each_alphabet_accumlative_sum(alphabet):
    Ss = [0]
    for i in S:
        Ss+=[Ss[-1] + (1 if i == alphabet else 0)]
    d[alphabet] = Ss

answer = []

for _ in range(q):
    alphabet,l,r = stdin.readline().strip().split()
    if alphabet not in d.keys():
        each_alphabet_accumlative_sum(alphabet)
    answer.append(d[alphabet][int(r)+1]-d[alphabet][int(l)])

print(*answer,sep='\n')
