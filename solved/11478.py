import sys

S = sys.stdin.readline().strip()

temp = []

diff = 1
i = 0
while diff <= len(S):
    if i+diff > len(S):
        i=0
        diff+=1
    else:
        temp.append(S[i:i+diff])
        i+=1

print(len(set(temp)))
