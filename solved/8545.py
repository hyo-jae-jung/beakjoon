from sys import stdin  

W = stdin.readline().strip()

ans = ''

for i in range(len(W)-1,-1,-1):
    ans+=W[i]

print(ans)
