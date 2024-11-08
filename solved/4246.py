from sys import stdin  

ans = []
while (n:=int(stdin.readline().strip())) != 0:
    s = stdin.readline().strip()
    t = ''
    for i in range(len(s)//n):
        t2 = ''
        if i%2 != 0:
            for j in range(n-1,-1,-1):
                t2+=s[i*n+j]
        else:
            for j in range(n):
                t2+=s[i*n+j]
        t+=t2

    a = ''
    for i in range(n):
        for j in range(i,len(t),n):
            a+=t[j]
    
    ans.append(a)

print(*ans,sep='\n')
