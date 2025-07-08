from sys import stdin  

N = int(stdin.readline().strip())
A = []
T = 10**8
for _ in range(N):
    x = (int(stdin.readline().strip()) + 5000)*T
    A.append(x)

A.sort()

mean = list(str(sum(A)//N - 5000*T))
if N%2 == 0:
    median = list(str((A[N//2 - 1] + A[N//2])//2 - 5000*T))
else:
    median = list(str(A[N//2] - 5000*T))

ans = []

def solution(x:list):
    tmp = ''
    i = 0
    while x:
        n = x.pop()
        if i == 8:
            tmp = '.'+tmp
        tmp = n+tmp
        i+=1
    return tmp

print(solution(mean))
print(solution(median))
