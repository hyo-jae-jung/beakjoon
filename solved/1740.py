from sys import stdin  

N = int(stdin.readline().strip())
ans = 0
i = 0
b = bin(N)

while (v:=b[-(i+1)]) != 'b':
    if v == '1':
        ans+=3**i
    i+=1

print(ans)
