from sys import stdin  

N = int(stdin.readline().strip())
S = stdin.readline().strip()

w = 1
p = 5
ans = 0

for i in S:
    if i == 'W':
        w+=1
    else:
        if w == 2 and p != 6:
            p = 6
        else:
            if p == 5:
                p = 1
            elif p == 1:
                p = 5
        
    if w == 3:
        ans = p
        break

print(ans)
