from sys import stdin  

_ = int(stdin.readline().strip())
S = stdin.readline().strip()

fox_like_words = ['u','o','s','p','c']

d = {}
for i in fox_like_words:
    d.update({i:0})

for i in S:
    if i in fox_like_words:
        d[i]+=1

print(min(d.values()))
