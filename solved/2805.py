from sys import stdin

N,M = map(int,stdin.readline().strip().split())
trees = [int(i) for i in stdin.readline().strip().split()]

high = max(trees)
row = 0
mid = (high + row)//2

while row <= high:
    if sum(i-mid if i>=mid else 0 for i in trees) >= M:
        row = mid + 1
    else:
        high = mid - 1
    mid = (high+row)//2

print(mid)

