from sys import stdin 
from itertools import permutations as perm

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    tmp = []
    k = int(stdin.readline().strip())

    is_p = []
    for _ in range(k):
        is_p.append(stdin.readline().strip())

    concat = [''.join(i) for i in perm(is_p,2)]

    for word in concat:
        seq = len(word)//2 + (1 if len(word)%2 > 0 else 0)
        for i in range(seq):
            if word[i] != word[-1*(i+1)]:
                break
        else:
            tmp.append(word)
    if tmp:
        ans.append(tmp)
    else:
        ans.append([0])

for i in ans:
    print(i[0],sep='\n')
