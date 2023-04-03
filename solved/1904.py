from sys import stdin 

N = int(stdin.readline().strip())
a,b = 1,2

if N == 1:
    print(a)
elif N == 2:
    print(b)
else:
    for _ in range(N-2):
        a,b = b%15746,(a+b)%15746
    print(b%15746)
