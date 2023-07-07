from sys import stdin 
from collections import defaultdict 

n = int(stdin.readline().strip())

def t(arr):
    answer = []
    for j in range(2):
        temp = []
        for i in range(2):
            temp.append(arr[i][j])
        answer.append(temp)
    return answer

def multi_arr(a,b):
    answer = []
    for i in range(2):
        temp = []
        for j in range(2):
            temp.append(sum(x*y for x,y in zip(a[i],b[j]))%1000000007)
        answer.append(temp)
    return answer

metrixes = defaultdict(list)
metrixes[1] = [[1,1],[1,0]]

def division(n):
    
    if metrixes[n]:
        return metrixes[n]
    
    div1 = n//2
    div2 = n-div1
    a = metrixes[div1] if metrixes[div1] else division(div1)
    b = metrixes[div2] if metrixes[div2] else division(div2)

    metrixes[n] = multi_arr(a,t(b))
    return metrixes[n]

print(division(n)[0][1])
