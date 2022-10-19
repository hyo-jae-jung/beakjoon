from itertools import permutations
N,M = input().split()
[print(" ".join(list(map(str,i)))) for i in permutations(range(1,int(N)+1),int(M))]