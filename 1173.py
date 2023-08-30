from sys import stdin 

N,m,M,T,R = [int(i) for i in stdin.readline().strip().split()]

cnt = 0
time = 0
X = m
while cnt < N:

    if X+T <= M:
        X+=T
        cnt+=1
    else:
        if X == m:
            print(-1)
            break
        X=max(X-R,m)
    time+=1
else:
    print(time)
