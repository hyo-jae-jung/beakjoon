from sys import stdin  

N,Q = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

perfix_xor = [0]
for i in range(N):
    perfix_xor.append(perfix_xor[-1] ^ A[i])

ans = 0
for _ in range(Q):
    s,e = map(int,stdin.readline().strip().split())
    s-=1
    ans^=perfix_xor[e] ^ perfix_xor[s]

print(ans)
