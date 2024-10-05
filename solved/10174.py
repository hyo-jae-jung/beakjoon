from sys import stdin  

n = int(stdin.readline().strip())
ans = ['Yes']*n

for j in range(n):
    w = stdin.readline().strip()
    for i in range(len(w)//2+(1 if len(w)%2 else 0)):
        if w[i].lower() != w[-1-i].lower():
            ans[j] = 'No'
            break

print(*ans,sep='\n')
