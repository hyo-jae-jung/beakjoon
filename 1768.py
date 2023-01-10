from sys import stdin 

c = int(stdin.readline().strip())
n = int(stdin.readline().strip())

answer = []

for _ in range(n):
    x,y = stdin.readline().strip().split()
    x = int(x)
    y = int(y)
    if x!=y and c-x == y-c:
        answer.append('yes')

if 'yes' in answer:
    print('yes')
