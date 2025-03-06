from sys import stdin   

n = int(stdin.readline().strip())
T = list(map(int,stdin.readline().strip().split()))

T.sort()
ans = 0

for i in range(n):
    ans+=T[i]*(2**i)

print(ans/2**n)
