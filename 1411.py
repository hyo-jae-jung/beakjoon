from sys import stdin
from collections import defaultdict 
from math import factorial as f

N = int(stdin.readline().strip())
converted_to_num = []
for _ in range(N):
    d = defaultdict(str)
    string = stdin.readline().strip()
    for i,j in enumerate(string,1):
        if not d[j]:
            d[j] = str(i)
    else:
        temp = ''
        for i in string:
            temp+=d[i]
    converted_to_num.append(temp)

d2 = defaultdict(int)
for i in converted_to_num:
    d2[i]+=1

def comb(a):
    if a == 1:
        return 0
    return a*(a-1)//2

answer = 0
for i in d2.values():
    answer+=comb(i)
    
print(answer)
