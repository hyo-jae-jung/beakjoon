from sys import stdin  

N = int(stdin.readline().strip())
reverse = ''
for i in bin(N)[2:].zfill(32):
    if i == '1':
        reverse+='0'
    else:
        reverse+='1'

ans = 0
for i,j in zip(bin(N)[2:].zfill(32),bin(int(reverse,2)+1)[2:]):
    if i != j:
        ans+=1

print(ans)
