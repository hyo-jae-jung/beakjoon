from sys import stdin 
import math

N = int(stdin.readline().strip())
street_trees = []
for i in range(N):
    street_trees.append(int(stdin.readline().strip()))

street_trees_diff = [street_trees[i] - street_trees[i-1] for i in range(1,len(street_trees))]
gcd = math.gcd(*street_trees_diff)
print(sum([i//gcd-1 for i in street_trees_diff]))
