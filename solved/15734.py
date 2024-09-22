from sys import stdin  

L,R,A = map(int,stdin.readline().strip().split())

ans = 0
m = min(L,R)
ans+=m*2
L,R=L-m,R-m

if L:
    mla = min(L,A) 
    ans+=mla*2
    L,A = L-mla,A-mla

elif R:
    mra = min(R,A) 
    ans+=mra*2
    R,A=R-mra,A-mra
    
if A:
    ans+=(A//2)*2

print(ans)
