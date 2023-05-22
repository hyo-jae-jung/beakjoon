from sys import stdin 

n = int(stdin.readline().strip())
works = []
for _ in range(n):
    works.append(tuple(map(int,stdin.readline().strip().split())))
works.sort(key=lambda x:x[1])

d,t = works.pop()

rt = t-d
while works:
    d,t = works.pop()
    if rt < t:
        rt = rt - d
    else:
        rt = t - d
else:
    print(rt)
    