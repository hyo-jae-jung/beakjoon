from sys import stdin

N,S = map(int,stdin.readline().strip().split())
numbers = list(map(int,stdin.readline().strip().split()))

numbers.sort()

ans = 0

def solution(n=0,v=0):

    if n >= N:
        return False

    solution(n+1,v)

    v+=numbers[n]

    if v == S:
        global ans
        ans+=1

    solution(n+1,v)

solution()
print(ans)
