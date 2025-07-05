from sys import stdin  

T = int(stdin.readline().strip())
ans = []

def decode(s):
    ss = ''
    l = int(len(s)**0.5)
    for i in range(1,l+1):
        for j in range(1,l+1):
            ss+=s[l*j-i]
    return ss

for _ in range(T):
    s = stdin.readline().strip()
    ans.append(decode(s))

print(*ans,sep='\n')
