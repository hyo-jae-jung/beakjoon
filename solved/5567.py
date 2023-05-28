from sys import stdin

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())

relationship = [set() for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,stdin.readline().strip().split())
    relationship[a].add(b)
    relationship[b].add(a)

answer_set = relationship[1]

for i in relationship[1]:
    answer_set = answer_set | relationship[i]

answer_set.discard(1)

print(len(answer_set))
