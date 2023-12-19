from sys import stdin 
import re

ans = ''
for i in stdin.readline().strip():
    if i.isupper():
        ans+=i

p = re.compile('U[A-Z]*C[A-Z]*P[A-Z]*C')

if bool(p.search(ans)):
    print('I love UCPC')
else:
    print('I hate UCPC')
