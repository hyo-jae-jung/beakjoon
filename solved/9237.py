from sys import stdin 

N = int(stdin.readline().strip())
trees = [int(i) for i in stdin.readline().strip().split()]
trees.sort(reverse=True)
print(max([i+j for i,j in enumerate(trees,1)])+1)
