from sys import stdin  

L = int(stdin.readline().strip())
R = int(stdin.readline().strip())

ans = 0
i = 0
while (tmp:=L*R//100) > 5:
    L = tmp
    i+=1
    ans+=tmp*(2**i)

print(ans)
