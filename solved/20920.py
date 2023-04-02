from sys import stdin 
from collections import defaultdict 
N,M = map(int,stdin.readline().strip().split())
vocabulary_d = defaultdict(list)
for _ in range(N):
    if len(word := stdin.readline().strip())  >= M:
        if vocabulary_d[word]:
            vocabulary_d[word][0]+=1
        else:
            vocabulary_d[word] = [1,len(word)]

vocabulary_l = []
for i,j in vocabulary_d.items():
    vocabulary_l.append((*j,i))
    
vocabulary_l.sort(key=lambda x:(-x[0],-x[1],x[2]))

for _,_,i in vocabulary_l:
    print(i)
    