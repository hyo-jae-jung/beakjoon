from sys import stdin  

N = int(stdin.readline().strip())
ab = list(map(int,stdin.readline().strip().split()))
a,b = min(ab),max(ab)

print(int(min(a,N-b)*'1' + min(N-a,b)*'0' + (N - min(a,N-b) - min(N-a,b))*'1',2) ^ int(min(a,N-b)*'0' + min(N-a,b)*'1' + (N - min(a,N-b) - min(N-a,b))*'1',2))
