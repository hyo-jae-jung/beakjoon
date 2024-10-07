from sys import stdin  

s = stdin.readline().strip()

ans = ''

i = 0

while i < len(s):
    ans+=s[i]
    if s[i] in set(['a','e','i','o','u']):
        i+=3
    else:
        i+=1

print(ans)
