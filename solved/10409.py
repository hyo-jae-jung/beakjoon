from sys import stdin 

n,T = map(int,stdin.readline().strip().split())

ans = 0
for i in list(map(int,stdin.readline().strip().split())):
    if T >= i:
        ans+=1
        T-=i
    else:
        break

print(ans)
