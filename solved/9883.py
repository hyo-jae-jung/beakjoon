from sys import stdin  

x,y = map(int,stdin.readline().strip().split())

ans = ''

for x_bit,y_bit in zip(bin(x)[2:].zfill(16),bin(y)[2:].zfill(16)):
    ans+=x_bit+y_bit

print(int(ans,2))
