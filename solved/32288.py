from sys import stdin   

n = int(stdin.readline().strip())
S = stdin.readline().strip()

ans = ''

for i in S:
    if i == 'I':
        ans+=i.lower()
    else:
        ans+=i.upper()

print(ans)
