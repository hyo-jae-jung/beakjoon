from sys import stdin  
	
e = stdin.read().strip()
lines = e.splitlines()

ans = []
while lines:
    b = lines.pop()
    a = lines.pop()

    cross = set(a) & set(b)
    t = []
    for i in cross:
        t+=[i]*min(a.count(i),b.count(i))

    ans.append(t)

for i in reversed(ans):
    print(''.join(sorted(i)))
