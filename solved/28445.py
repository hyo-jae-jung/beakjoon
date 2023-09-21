from sys import stdin 

father = stdin.readline().strip().split()
mother = stdin.readline().strip().split()

colors = father+mother
colors_set = []
for i in colors:
    if i not in colors_set:
        colors_set.append(i)
else:
    colors_set.sort()

l = len(colors_set)
answer = []
for i in range(l):
    for j in range(l):
        answer.append((colors_set[i],colors_set[j]))

for i in answer:
    print(*i)
