from sys import stdin 
from itertools import permutations as perm

N = int(stdin.readline().strip())
people = []
for i in range(1,N+1):    
    people.append((i,max(map(lambda x: int(str(sum(x))[-1]),perm(list(map(int,stdin.readline().strip().split())),3)))))

people.sort(key=lambda x:x[0])

print(people[0][0])
