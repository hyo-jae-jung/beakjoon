from sys import stdin  

N = int(stdin.readline().strip())
MOD = 1000000007

g = [1,2,7]
prefix_sum = 0
for i in range(3,10**6+1):
    prefix_sum+=g[i-3]%MOD
    g.append((2*g[i-1] + 3*g[i-2] + 2*prefix_sum)%MOD)

print(g[N])
