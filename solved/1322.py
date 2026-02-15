from sys import stdin  

X,K = map(int,stdin.readline().strip().split())
ans = 0
i,j = 0,0

while K >= (1 << j):
    if X & (1 << i) == 0:
        if K & (1 << j) == (1 << j):
            ans+=(1 << i)
        j+=1
    i+=1

print(ans)
