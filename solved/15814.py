from sys import stdin  

S = stdin.readline().strip()
T = int(stdin.readline().strip())
idx = list(range(len(S)))
ans = ''
for _ in range(T):
    A,B = map(int,stdin.readline().strip().split())
    idx[A],idx[B] = idx[B],idx[A]

for i in idx:
    ans+=S[i]

print(ans)
