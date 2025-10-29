from sys import stdin   

N = int(stdin.readline().strip())
people = []
for _ in range(N):
    people.extend(list(map(lambda x:tuple(x.split('-')),stdin.readline().strip().split())))
    people = list(map(lambda item: (item[0],int(item[1])),people))

d = {}
for i,t in enumerate(sorted(people),1):
    d.update({t:i})

rank = [0]*5*N

for i in range(5*N):
    rank[i] = d[people[i]]

target = 1
stack = []
ans = 'GOOD'

for i in rank:

    if i == target:
        target+=1
    else:
        if stack and stack[-1] < i:
            ans = 'BAD'
            break
        stack.append(i)

    while stack and stack[-1] == target:
        stack.pop()
        target+=1

print(ans)
    