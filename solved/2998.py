from sys import stdin 

b = stdin.readline().strip()

rest = len(b)%3
if rest:
    b = '0'*(3-rest) + b

d = {}
for i in range(8):
    d[str(bin(i)[2:]).zfill(3)] = str(i)

ans = ''
for i in range(0,len(b),3):
    ans+=d[str(b[i:i+3])]

print(ans)
