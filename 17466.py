import sys
sys.setrecursionlimit(10**7)

N,P = map(int,sys.stdin.readline().strip().split())

ans = 1
for i in range(1,N+1):
    ans*=(i%P)

print(ans%P)
