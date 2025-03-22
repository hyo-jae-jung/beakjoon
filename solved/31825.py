from sys import stdin  

N,Q = map(int,stdin.readline().strip().split())
bunch_of_alphabet = list(stdin.readline().strip())

def count_alphabet_bunch(S,l,r):
    cnt = 1
    criteria = S[l-1]
    for i in range(l-1,r):
        if S[i] != criteria:
            cnt+=1
            criteria = S[i]
    return cnt

def change_alphabet(S,l,r):
    for i in range(l-1,r):
        S[i] = chr(((ord(S[i])-65)+1)%26+65)
    return S

ans = []
for _ in range(Q):
    q,l,r = map(int,stdin.readline().strip().split())
    if q == 1:
        ans.append(count_alphabet_bunch(bunch_of_alphabet,l,r))
    else:
        bunch_of_alphabet = change_alphabet(bunch_of_alphabet,l,r)

print(*ans,sep='\n')
