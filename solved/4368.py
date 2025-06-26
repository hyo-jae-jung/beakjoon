from sys import stdin  

lines = stdin.read().strip().splitlines()
ans = []
d = {}
switch = True
for line in lines:
    
    if line == '':
        switch = False
        continue

    if switch:
        a,b = line.split()
        d.update({b:a})
    else:
        if d.get(line):
            ans.append(d[line])
        else:
            ans.append('eh')

print(*ans,sep='\n')
