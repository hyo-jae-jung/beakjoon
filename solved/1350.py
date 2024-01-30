from sys import stdin 

N = int(stdin.readline().strip())
ans = 0
files = list(map(int,stdin.readline().strip().split()))
cluster = int(stdin.readline().strip())
for i in files:
    ans+=(i//cluster+(1 if i%cluster > 0 else 0))*cluster

print(ans)
