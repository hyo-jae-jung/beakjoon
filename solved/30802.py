from sys import stdin  

N = int(stdin.readline().strip())
SIZE = list(map(int,stdin.readline().strip().split()))
T,P = map(int,stdin.readline().strip().split())

a = 0
for i in SIZE:
    a+=i//T + (1 if i%T > 0 else 0)

print(a)
print(b:=N//P, N-P*b)
