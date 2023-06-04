from sys import stdin 
from math import factorial as f

N,M,K = map(int,stdin.readline().strip().split())

if f(N+M)//(f(N)*f(M)) < K:
    answer = -1
else:
    k = K-1
    boundary = M+1
    share = k//boundary
    rest = k%boundary

    temp = ''
    for i in range(boundary):
        if i == rest:
            temp+='a'
        else:
            temp+='z'
    
    answer = (N-1-share)*'a'+ temp + 'a'*share

print(answer)
