from sys import stdin  

S = stdin.readline().strip()
P = stdin.readline().strip()

ans = 'No'

def case_reversal(S):
    tmp = ''
    for s in S:
        if s.isupper():
            tmp+=s.lower()
        elif s.islower():
            tmp+=s.upper()
        elif s.isnumeric():
            tmp+=s
    return tmp

if len(S) == len(P):
    if S == P:
        ans = 'Yes'
    else:        
        if case_reversal(S) == P:
            ans = 'Yes'
elif len(S) == len(P) + 1:
    if (S[1:] == P or case_reversal(S[1:]) == P) and S[0].isnumeric():
        ans = 'Yes'
    elif (S[:-1] == P or case_reversal(S[:-1]) == P) and S[-1].isnumeric():
        ans = 'Yes'
elif len(S) == len(P) + 2:
    if S[0].isnumeric() and S[-1].isnumeric() and (S[1:-1] == P or case_reversal(S[1:-1]) == P):
        ans = 'Yes'

print(ans)
