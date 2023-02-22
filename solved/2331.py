from sys import stdin 

A,P = map(int,stdin.readline().strip().split())
D = [A]

def solution(num:int,p:int)->int:
    answer = 0
    for i in map(int,list(str(num))):
        answer+=i**p
    return answer
    
temp = A
while True:
    temp = solution(temp,P)
    if temp in D:
        break
    else:
        D.append(temp)
    
print(D.index(temp))
