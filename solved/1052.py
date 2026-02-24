from sys import stdin  

N,K = map(int,stdin.readline().strip().split())

if N < K:
    print(0)
else:
    while N > 0 and K > 0:
        i = 0
        while N > (1<<i):
            i+=1
        
        if N == (1<<i):
            print(0)
            break
        
        if K > 1:
            i-=1
        K-=1
        N-=(1<<i)
    else:
        print(-N)
