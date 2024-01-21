from sys import stdin 
from collections import deque

T = int(stdin.readline().strip())

def is_same(l:list) -> bool:
    return all([l[0]==i for i in l])

def add_candy(l:list) -> list:
    tmp = []
    for i in l:
        t = i
        if i%2 != 0:
            t+=1
        tmp.append(t)
    return tmp

def solution(tmp:list) -> list:
    tmp2 = deque([])
    for i in range(len(tmp)):
        tmp2.append(tmp[i]//2)
        tmp[i] = tmp[i]//2
    t = tmp2.pop()
    tmp2.appendleft(t)
    return [i+j for i,j in zip(tmp,tmp2)]

ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    candys = list(map(int,stdin.readline().strip().split()))
    cnt = 0

    while True:
        candys = add_candy(candys)
        if is_same(candys):
            break
        candys = solution(candys)
        cnt+=1
    ans.append(cnt)

print(*ans,sep='\n')
