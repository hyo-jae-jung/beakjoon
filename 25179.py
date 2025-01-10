from sys import stdin  

N,M = map(int,stdin.readline().strip().split())

print(N//M,N%M,(N//M)%2)
if N == 1:
    print("Can't win")
elif M>=N:
    print("Can win")
elif M == 1 or N%M > 0:
    print("Can't win" if (N//M)%2 == 0 else "Can win")
elif N%M == 0:
    print("Can win" if (N//M)%2 == 1 else "Can't win")
