from sys import stdin 

K,D,A = map(int,stdin.readline().strip().split('/'))
if K+A < D or D == 0:
    print('hasu')
else:
    print('gosu')
    