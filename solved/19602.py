from sys import stdin  

S = int(stdin.readline().strip())
M = int(stdin.readline().strip())
L = int(stdin.readline().strip())

print('happy' if S+2*M+3*L >= 10 else 'sad')
