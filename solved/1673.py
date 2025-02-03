from sys import stdin   

ans = []

while s:=stdin.readline().strip():
    n,k = map(int,s.split())
    t = n
    while n >= k:
        t+=n//k
        n = n//k + n%k
    ans.append(t)

print(*ans,sep='\n')
