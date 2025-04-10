from sys import stdin   

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    a,b = map(int,stdin.readline().strip().split())
    d = {}
    val = []
    idx = 0
    while a > 0:

        if not d.get(a):
            d.update({a:idx})
            idx+=1
            val.append(str(a//b))
            a = a%b
            a*=10
            continue

        if d.get(a):
            break

    s = ''
    s+=val[0]+'.'
    if a > 0:
        for i in range(1,len(val)):
            if d.get(a) == i:
                s+='('
            s+=val[i]
        else:
            s+=')'
    else:
        s+=''.join(val[1:])+'(0)'

    ans.append(s)

print(*ans,sep='\n')
