from sys import stdin  

n,m = map(int,stdin.readline().strip().split())

def solution(n,k):
    result = 0
    while (cnt:=n//k) > 0:
        result+=cnt
        n = cnt
    return result

v5 = solution(n,5) - solution(m,5) - solution(n-m,5)
v2 = solution(n,2) - solution(m,2) - solution(n-m,2)

print(min(v5,v2))
