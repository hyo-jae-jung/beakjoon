from sys import stdin  

n = int(stdin.readline().strip())
ans = 1

while n!=1:
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n+1
    ans+=1

print(ans)
