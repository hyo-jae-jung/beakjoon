from sys import stdin 

N = int(stdin.readline().strip())

for i in list(range((2*N-1)//2))+[(2*N-1)//2]+list(reversed(list(range((2*N-1)//2)))):
    print(' '*((2*N-1)//2-i) + '*'*(2*i+1))
    