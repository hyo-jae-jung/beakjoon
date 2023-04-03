from sys import stdin 

N = int(stdin.readline().strip())
data = []
for _ in range(N):
    a = stdin.readline().strip()
    b = len(a)
    c = 0
    for i in a:
        try:
            c+=int(i)
        except:
            pass
    data.append((a,b,c))

data.sort(key=lambda x:(x[1],x[2],x[0]))

for i,_,_ in data:
    print(i)
    