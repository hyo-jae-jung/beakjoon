from sys import stdin

eigen_num = map(int,stdin.readline().strip().split())
print(sum([i**2 for i in eigen_num])%10)
