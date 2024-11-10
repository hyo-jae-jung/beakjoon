from sys import stdin  

A,B = map(int,stdin.readline().strip().split())
K,X = map(int,stdin.readline().strip().split())

xk,kx = K-X,K+X

if kx < A:
    print('IMPOSSIBLE')
elif A <= xk and kx <= B:
    print(kx-xk+1)
elif xk <= A and B <= kx:
    print(B-A+1)
elif xk <= A and A <= kx:
    print(kx-A+1)
elif A <= xk and xk <= B:
    print(B-xk+1)
elif xk > B:
    print('IMPOSSIBLE')
