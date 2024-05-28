from sys import stdin 

n = int(stdin.readline().strip())
students = stdin.readline().strip().split()
d = {}
for i in students:
    d.update({i:0})

for _ in range(n):
    likes = stdin.readline().strip().split()
    for i in likes:
        d[i]+=1

for i in sorted(d.items(),key=lambda x:(-x[1])):
    print(*i)

