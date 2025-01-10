from sys import stdin  

X,C,K = map(int,stdin.readline().strip().split())
arr = []
for _ in range(K):
    arr.append(tuple(map(int,stdin.readline().strip().split())))

arr.sort(key=lambda x:(x[0]))

d = {}

for _,c,n in arr:
    if not c in d.values():
        if d.get(n) == c:
            d.pop(n)
        d.update({n:c})

for i in sorted(d.items(),key=lambda x:(x[0])):
    print(*i)
