from sys import stdin  

ans = []
while (i:=stdin.readline().strip()) != '0 0 0':
    a1,a2,a3 = map(int,i.split())
    if a3 - a2 == a2 - a1:
        ans.append(f'AP {a3 + a2 - a1}')
    else:
        ans.append(f'GP {a3*(a2//a1)}')

print(*ans,sep='\n')
