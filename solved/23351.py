from sys import stdin  

N,K,A,B = map(int,stdin.readline().strip().split())
flowerpot = [K]*N
ans = 0
idx = 0

while all(map(lambda x:x > 0,flowerpot)):
    ans+=1
    for i in range(A):
        flowerpot[idx]+=B
        idx = (idx+1)%N
    
    flowerpot = list(map(lambda x:x-1,flowerpot))

print(ans)
