from sys import stdin 
from collections import defaultdict

N,B = map(int,stdin.readline().strip().split())
metrixes = defaultdict(list)

for _ in range(N):
    metrixes[1].append([int(i)%1000 for i in stdin.readline().strip().split()])

def t(a):
    b = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(a[j][i])
        b.append(temp)
    return b

def multi_arr(a,b):
    answer = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(sum(x*y for x,y in zip(a[i],b[j]))%1000)
        answer.append(temp)
    
    return answer

def division(n):
    if metrixes[n]:
        return metrixes[n]
    
    div1 = n//2
    div2 = n-div1
    a = metrixes[div1] if metrixes[div1] else division(div1)
    b = metrixes[div2] if metrixes[div2] else division(div2)

    metrixes[n] = multi_arr(a,t(b))
    return metrixes[n]

for i in division(B):
    print(*i)
