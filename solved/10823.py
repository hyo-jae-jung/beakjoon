from sys import stdin 

S = stdin.read().replace('\n','').split(',')

print(sum(map(int,S)))
