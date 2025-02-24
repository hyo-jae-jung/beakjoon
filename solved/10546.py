from sys import stdin   

N = int(stdin.readline().strip())
s = set()
for _ in range(2*N-1):
    name = stdin.readline().strip()
    if name in s:
        s.discard(name)
    else:
        s.add(name)

print(*s)
