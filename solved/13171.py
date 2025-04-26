from sys import stdin  

A = int(stdin.readline())
X = int(stdin.readline())

MOD = 10**9+7
ans = 1

b = bin(X)[2:]

t = [A%MOD]
for _ in range(len(b)-1):
    t.append((t[-1]*t[-1])%MOD)

for i,j in enumerate(reversed(b)):
    if j == '1':
        ans = ((ans%MOD)*(t[i]%MOD))%MOD

print(ans)
