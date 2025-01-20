from sys import stdin 

d = {}
s=stdin.read()
for i in s:
    if d.get(i):
        d[i]+=1
    else:
        d.update({i:1})

if d.get('\n'):
    del d['\n']
if d.get(' '):
    del d[' ']

max_cnt = max(d.values())
ans = ''

for i,j in sorted(list(d.items()),key=lambda x:(-x[1],x[0])):
    if max_cnt == j:
        ans+=i
    else:
        break

print(ans)
