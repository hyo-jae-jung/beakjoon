from itertools import product, permutations
from sys import stdin

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    n = int(stdin.readline().strip())
    p = product(range(n+1),range(int(n/2)+1),range(int(n/3)+1))
    cnt = 0
    for i in p:
        x,y,z = i
        if x+2*y+3*z == n:
            for i in [''.join(map(str,i)) for i in set(permutations([1]*x+[2]*y+[3]*z))]:
                if not any(['11' in i, '22' in i, '33' in i]):
                    cnt+=1
    answer.append(int(cnt))

for i in answer:
    print(i)
