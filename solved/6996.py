from sys import stdin
from collections import defaultdict

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    before,after = stdin.readline().strip().split()
    d = defaultdict(int)
    for i in before:
        d[i]+=1

    for i in after:
        d[i]-=1

    s = ''
    for i in  d.values():
        if i != 0:
            s = "NOT "
            break
    answer.append(f"{before} & {after} are {s}anagrams.")

print(*answer,sep='\n')
