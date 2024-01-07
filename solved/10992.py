from sys import stdin 

N = int(stdin.readline().strip())
print(' '*(N-1)+'*')
for i in range(1,N-1):
    print(' '*(N-1-i)+'*'+' '*(2*i-1)+'*')
if N > 1:
    print('*'*(2*N-1))
