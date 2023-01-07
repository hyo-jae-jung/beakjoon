from sys import stdin

N,M = map(int,stdin.readline().strip().split())
trees = map(int,stdin.readline().strip().split())

trees = sorted(trees,reverse=True)

H = max(trees)

