from sys import stdin 

N = int(stdin.readline().strip())
S = []

for i in range(N):
    tmp = stdin.readline().strip()
    if tmp == '?':
        loc = i
    S.append(tmp)

first_alphabet = S[loc-1][-1] if loc > 0 else False
last_alphabet = S[loc+1][0] if loc < N-1 else False
M = int(stdin.readline().strip())

for _ in range(M):
    tmp = stdin.readline().strip()
    if tmp in S:
        continue
    if bool(first_alphabet) & bool(last_alphabet):
        if first_alphabet == tmp[0] and last_alphabet == tmp[-1]:
            ans = tmp
    elif bool(first_alphabet):
        if first_alphabet == tmp[0]:
            ans = tmp
    elif bool(last_alphabet):
        if last_alphabet == tmp[-1]:
            ans = tmp
    else:
        ans = tmp
print(ans)
