from sys import stdin  

T = int(stdin.readline().strip())
ans = 0
i = 4
while T > 0:
    ans+=(T//(9**i))*10**i
    T = T%(9**i)
    i-=1

print(ans)
