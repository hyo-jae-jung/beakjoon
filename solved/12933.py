from sys import stdin  

s = stdin.readline().strip()
sound = 'quack'
d = {'q':0,'u':1,'a':2,'c':3,'k':4}
ans = 0
ducks = []
for i in s:
    if ans != -1:
        if not ducks:
            if i == 'q':
                ducks.append(i)
                continue
            else:
                ans = -1
                break

        j = 0
        while j < len(ducks):
            if ducks[j][-1] == sound[(d[i]-1)%5]:
                ducks[j]+=i
                break
            j+=1
        else:
            if i == 'q':
                ducks.append(i)
            else:
                ans = -1
                break

if ans == -1:
    print(ans)
else:
    for i in ducks:
        if i[-1] == 'k':
            ans+=1
        else:
            ans = -1
            break
    print(ans)
