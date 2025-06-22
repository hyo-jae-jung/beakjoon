from sys import stdin   

N = int(stdin.readline().strip())
X = sorted(list(map(int,stdin.readline().strip().split())))

print(sum(map(lambda x:x/2,X[:-1])) + X[-1])
