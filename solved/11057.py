import sys

N = int(sys.stdin.readline().strip())

def f(n=1):
    i = 1
    arr = list(range(1,11))
    while i < n:
        for j in range(1,10):
            arr[j] = (arr[j] + arr[j-1])%10007
        i+=1
    return arr[-1]

print(f(N))
