from sys import stdin 

N = int(stdin.readline().strip())
children = [0] + [int(i) for i in stdin.readline().strip().split()]
D = [0]
for i in range(1,len(children)):
    for j in range(i):
        if children[i] > children[j]:
            try:D[i] = max(D[i],D[j]+1)
            except:D.append(1)

print(D)
