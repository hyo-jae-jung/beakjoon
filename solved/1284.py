from sys import stdin  

ans = []
while (num:=stdin.readline().strip()) != '0':
    cm = 1 + len(num)
    for i in num:
        if i == '1':
            cm+=2
        elif i == '0':
            cm+=4
        else:
            cm+=3
    ans.append(cm)

print(*ans,sep='\n')
