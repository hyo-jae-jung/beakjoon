from sys import stdin  

ans = []
while (t:=stdin.readline().strip()) != '0':
    b,p,m = map(int,t.split())
    a = ''
    tmp=int(str(p),b)%int(str(m),b)
    while b <= tmp:
        a = str(tmp%b) + a
        tmp = tmp//b
    else:
        a = str(tmp) + a
    ans.append(a)
    
print(*ans,sep='\n')
