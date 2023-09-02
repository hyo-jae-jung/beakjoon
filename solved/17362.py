from sys import stdin 

n = int(stdin.readline().strip())
d = dict()
for i,j in zip(range(8),[1,2,3,4,5,4,3,2]):
    d.update({i:j})

print(d[(n-1)%8])
