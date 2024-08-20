from sys import stdin  

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    tmp = stdin.readline().strip().split()
    tmp.extend(tmp[:2])
    ans.append(tmp[2:])

for i in ans:
    print(*i)
