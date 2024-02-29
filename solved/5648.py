from sys import stdin 

l = []
l.extend(stdin.readline().strip().split())
m = []

while (int(l[0]) - len(l) + 1) > len(m):
    m.extend(stdin.readline().strip().split())

for i in sorted(map(lambda x:int(''.join(reversed(x))),l[1:]+m)):
    print(i)
