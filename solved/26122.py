from sys import stdin   

K = int(stdin.readline().strip())
S = stdin.readline().strip()
ans = 0
p = ''
a,b = 0,0
for i in S:
    if p != i:
        ans = max(ans,min(a,b)*2)
        b = a
        a = 1
        p = i
    else:
        a+=1
else:
    ans = max(ans,min(a,b)*2)

print(ans)
