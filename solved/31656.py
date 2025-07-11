from sys import stdin   

S = stdin.readline()[:-1]

ans = ''
for i in S:
    if ans[-1:] != i:
        ans+=i

print(ans)
