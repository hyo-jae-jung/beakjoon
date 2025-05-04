from sys import stdin  
from bisect import bisect_left

N = int(stdin.readline().strip())
soldiers = list(map(lambda x:-int(x),stdin.readline().strip().split()))
D = []
l = 0
for i in soldiers:
    loc = bisect_left(D,i)
    if l == loc:
        D.append(i)
        l+=1
    else:
        D[loc] = i

print(N - l)
