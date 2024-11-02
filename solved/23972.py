from sys import stdin

K,N = map(int,stdin.readline().strip().split())

if N == 1:
    print(-1)
else:
    print(K+K//(N-1) + (0 if K/(N-1) == K//(N-1) else 1))
