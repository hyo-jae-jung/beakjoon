from sys import stdin  

N = int(stdin.readline().strip())

ans = 0

while N > 1:
    if N%2 == 0:
        N = N//2
    else:
        N+=1
        N = N//2
    ans+=1

print(ans+N)
