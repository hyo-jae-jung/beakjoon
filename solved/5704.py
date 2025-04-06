from sys import stdin  

ans = []
while (s:=stdin.readline().strip()) != '*':
    bundle = set()
    for i in range(26):
        bundle.add(chr(97+i))

    for i in s:
        if i:
            bundle.discard(i)
    
    if bundle:
        ans.append('N')
    else:
        ans.append('Y')

print(*ans,sep='\n')
