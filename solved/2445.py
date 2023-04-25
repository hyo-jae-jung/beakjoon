from sys import stdin 

N = int(stdin.readline().strip())

for i in range(-1*(N-1),N):
    print('*'*(N-abs(i))+' '*abs(i)*2 + '*'*(N-abs(i)))
    