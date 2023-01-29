from sys import stdin 

N = int(stdin.readline().strip())
S = dict.fromkeys(['STRAWBERRY', 'BANANA', 'LIME', 'PLUM'],0)
for _ in range(N):
    fruit,cnt = stdin.readline().strip().split()
    S[fruit]+=int(cnt)

if 5 in S.values():
    print('YES')
else:
    print('NO')
