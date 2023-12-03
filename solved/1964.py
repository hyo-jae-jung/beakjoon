from sys import stdin 

N = int(stdin.readline().strip())

def solution(n):
    return 1 + (3*n**2 + 5*n)//2

print(solution(N)%45678)
