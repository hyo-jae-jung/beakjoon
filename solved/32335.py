from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
S = stdin.readline().strip()
ans = ''
for i in S[:-1]:
    num = int(i)
    if num == 0:
        ans+=i
    else:
        if M >= 10-num:
            M-=(10-num)
            ans+='0'
        else:
            ans+=i

if M > 0:
    ans+=str((int(S[-1]) + M)%10)
else:
    ans+=S[-1]

print(ans)
