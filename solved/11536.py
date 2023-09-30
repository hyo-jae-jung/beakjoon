from sys import stdin 

N = int(stdin.readline().strip())
names = []
for _ in range(N):
    names.append(stdin.readline().strip())

increasing = ''.join(sorted(names))
decreasing = ''.join(sorted(names,reverse=True))
namess = ''.join(names)

if namess == increasing:
    print("INCREASING")
elif namess == decreasing:
    print("DECREASING")
else:
    print("NEITHER")
