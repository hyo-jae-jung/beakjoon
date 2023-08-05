import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline().strip())
wines = []
for _ in range(n):
    wines.append(int(sys.stdin.readline().strip()))

memo = [[-1]*2 for _ in range(n)]

def max_drink(wine_idx=n,stack=):