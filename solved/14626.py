from sys import stdin   

ISBN = list(stdin.readline().strip())

star_idx = ISBN.index('*')
r = (10 - int(ISBN[-1]))%10

t = 0
for i in range(12):
    if ISBN[i] != '*':
        tmp = int(ISBN[i])
        t+=tmp*(3 if i%2 else 1)

for i in range(10):
    if (t+i*(3 if star_idx%2 else 1))%10 == r:
        print(i)
        break
    