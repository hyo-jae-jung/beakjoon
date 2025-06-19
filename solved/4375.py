from sys import stdin  

e = stdin.read().strip()
lines = e.splitlines()
ans = []
for line in map(int,lines):
    i = 1
    while int('1'*i)%line > 0:
        i+=1
    ans.append(i)

print(*ans,sep='\n')
