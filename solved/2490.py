from sys import stdin 

answer = []
for _ in range(3):
    answer.append(list(stdin.readline().strip().split()).count('0'))
d = dict()
for i in range(1,5):
    d.update({i:chr(64+i)})
d.update({0:'E'})
for i in answer:
    print(d[i])
