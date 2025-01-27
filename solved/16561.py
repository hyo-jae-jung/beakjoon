import sys
sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline().strip())

mult_cnt = -3
while n > 0:
    n-=3
    mult_cnt+=1

def f(n):
    if n == 0:
        return 1
    return n*f(n-1)

print(f(mult_cnt+2)//(f(2)*f(mult_cnt)))
