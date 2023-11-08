from sys import stdin 

s = stdin.readline().strip()

ans = 26 if s[0] == 'c' else 10
for i in range(1,len(s)):
    if s[i] == 'c' and s[i-1] == 'c':
        ans*=25
    elif s[i] == 'c' and s[i-1] == 'd':
        ans*=26
    elif s[i] == 'd' and s[i-1] == 'd':
        ans*=9
    else:
        ans*=10

print(ans)
