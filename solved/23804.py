from sys import stdin  

N = int(stdin.readline().strip())

for _ in range(N):
    print("@"*(5*N))

for _ in range(3*N):
    print("@"*N)

for _ in range(N):
    print("@"*(5*N))
