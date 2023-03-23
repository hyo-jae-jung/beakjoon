from sys import stdin
from collections import defaultdict

A,B = map(int,stdin.readline().strip().split())

factorize_cnt_map = defaultdict(int)

def factorize_cnt_with_recursion(n:int,cnt:int=0,div:int=2,accumlative_n:int=1)->int:
    if factorize_cnt_map[n]:
        cnt+=factorize_cnt_map[n]
        n = 1
    if n == 1:
        return cnt
    while n%div != 0:
        div+=1
    else:
        cnt+=1
        n = n//div
        accumlative_n*=div
        factorize_cnt_map[accumlative_n]=cnt
        return factorize_cnt_with_recursion(n,cnt,div,accumlative_n)

def check_prime(n:int)->list:
    sieve = [False,False]+[True]*(n-1)
    for i in range(2,int(n**0.5)+1):
        if sieve[i] == True:
            for j in range(i+i,n+1,i):
                sieve[j] = False
    return sieve

answer = 0
sieve = check_prime(B)

for i in range(A,B+1):
    if not sieve[i]:
        answer+=sieve[factorize_cnt_with_recursion(i)]

print(answer)
