from sys import stdin  

D,K = map(int,stdin.readline().strip().split())

a,b = 1,0
for _ in range(D-1):
    c = a+b 
    a = b
    b = c

def solution(a,b):
    for i in range(1,K//a+1):
        for j in range(1,K//b+1):
            if a*i+b*j == K:
                return i,j
    
print(*solution(a,b),sep='\n')
