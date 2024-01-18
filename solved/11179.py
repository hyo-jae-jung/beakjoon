from sys import stdin 

s = bin(int(stdin.readline().strip()))[2:]
ans = 0
for i,j in enumerate(s):
    ans+=(2**i)*int(j)

print(ans)
