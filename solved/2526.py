from sys import stdin  

N,P = map(int,stdin.readline().strip().split())
d = {}
n = N
i = 0

while not d.get(n):
    d.update({n:i})
    n = n*N%P
    i+=1

print(i - d[n])
