from sys import stdin  

d = {
"Bessie":0,
"Elsie":0,
"Daisy":0,
"Gertie":0,
"Annabelle":0,
"Maggie":0,
"Henrietta":0,
}

N = int(stdin.readline().strip())
for _ in range(N):
    name,cnt = stdin.readline().strip().split()
    d[name]+=int(cnt)

q = {}
for name,cnt in d.items():
    if not q.get(cnt):
        q.update({cnt:[]})
    q[cnt].append(name)

r = sorted(q.items(),key = lambda x:x[0])

if len(r) == 1:
    print("Tie")
elif len(r[1][1]) > 1:
    print("Tie")
else:
    print(*r[1][1])
    