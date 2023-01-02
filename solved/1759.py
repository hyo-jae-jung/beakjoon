from sys import stdin
from itertools import product, combinations

L,C = map(int,stdin.readline().strip().split())

inp = set(stdin.readline().strip().split())
vowel = set(['a', 'e', 'i', 'o', 'u'])

intersection = vowel & inp
diff = inp - vowel

answer = []

for i in range(1,len(intersection)+1):
    j = L-i
    if j >=2:
        for k,l in product(combinations(intersection,i),combinations(diff,j)):
            answer.append(''.join(sorted(list(k)+list(l))))

for i in sorted(answer):
    print(i)
