from sys import stdin  

n,k = map(int,stdin.readline().strip().split())

def change(N,K):
    tmp = ''
    while N >= K:
        tmp = str(N%K) + tmp
        N = N//K
    else:
        tmp = str(N) + tmp
    return tmp

print(change(sum(map(int, [i.strip() for i in change(n,k).split('0') if i])),k))
