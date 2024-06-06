from sys import stdin  

N = int(stdin.readline().strip())

a = list(map(int,stdin.readline().strip().split()))

a.sort()

print(sum(a[:N//2]),sum(a[N//2:]))
