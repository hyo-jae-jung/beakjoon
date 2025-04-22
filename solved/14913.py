from sys import stdin  

a,d,k = map(int,stdin.readline().strip().split())
ans = (k+d-a)/d
if 1 > ans:
    print('X')
else:
    print(int(ans) if ans%int(ans) == 0 else 'X')

