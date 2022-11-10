import sys

T = int(sys.stdin.readline().strip())

answer = []

def GCD(a,b):
    l = max(a,b)
    m = min(a,b)
    while l%m != 0:
        temp = l%m
        l=m
        m=temp
    return m

for _ in range(T):
    A,B = map(int,sys.stdin.readline().strip().split())
    gcd = GCD(A,B)
    answer.append(A*B/gcd)
   
for i in answer:
    print(int(i))
