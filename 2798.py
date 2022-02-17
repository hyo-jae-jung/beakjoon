from itertools import combinations

N,M = input().split()
print(max([sum(i) for i in combinations([int(i) for i in input().split()],3) if sum(i) <= int(M)]))

