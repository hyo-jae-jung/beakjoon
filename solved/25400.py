from sys import stdin 

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))

I = 0
for i in A:
    if i == I+1:
        I+=1

print(N-I)
