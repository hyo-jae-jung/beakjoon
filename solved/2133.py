from sys import stdin  

N = int(stdin.readline().strip())

g = [0]*31
g[2]+=1
for i in range(2,31,2):
    g[i]+=2

f = [0]*31
f[2] = 3

for i in range(4,31,2):
    tmp = g[i]
    for j,k in enumerate(range(i,1,-2),1):
        tmp+=g[k]*f[i-k]
    f[i] = tmp

print(f[N])
