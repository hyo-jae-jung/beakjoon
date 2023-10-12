from sys import stdin 
from itertools import product

N,K = map(int,stdin.readline().strip().split())
nums = list(map(str,stdin.readline().strip().split()))
l = len(str(N))
def solution(l):
    while l > 0:
        tmp = [int(''.join(i)) for i in list(product(nums,repeat=l))]
        for i in sorted(tmp,reverse=True):
            if i <= N:
                return i
        l-=1

print(solution(l))
