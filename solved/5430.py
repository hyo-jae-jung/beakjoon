from sys import stdin 
from collections import deque 

T = int(stdin.readline().strip())

def fn(d:deque,r_cnt:int,d_cnt:int):
    try:
        if r_cnt%2 == 0:
            for _ in range(d_cnt):
                d.popleft()
        else:
            for _ in range(d_cnt):
                d.pop()
    except:
        return 'error'
    return d

inps = []

for _ in range(T):
    
    fn_keys = deque(stdin.readline().strip())
    stdin.readline()
    exec('l = deque([int(i) for i in stdin.readline().strip().lstrip(\'[\').rstrip(\']\').split(\',\') if i])')
    inps.append([fn_keys,l])

def solution(l:list):
    
    fn_keys = l[0]
    li = l[1]

    r_cnt = 0
    d_cnt = 0
    while fn_keys:
        temp = fn_keys.popleft()
        if temp == 'R':
            r_cnt+=1
        else:
            d_cnt+=1

        if fn_keys:
            if temp == 'D' and fn_keys[0] == 'R':
                li = fn(li,r_cnt,d_cnt)
                d_cnt=0
        else:
            li = fn(li,r_cnt,d_cnt)
    
    if isinstance(li,str):
        return li
    else:
        if r_cnt%2 == 0:
            return li
        else:
            answer = deque()
            while li:
                answer.append(li.pop())
            return answer

for i in inps:
    temp = solution(i)
    if temp == 'error':
        print(temp)
    else:
        print('['+','.join([str(i) for i in temp])+']')
    