from sys import stdin  

ans = []
while (n0:=int(stdin.readline().strip())) != 0:
    n1 = 3*n0
    if n1%2 == 0:
        t = 'even'
        n2 = n1//2
    else:
        t = 'odd'
        n2 = (n1+1)//2
    n3 = 3*n2
    n4 = n3//9
    t+=" " + str(n4)

    ans.append(t)

for i in range(1,len(ans)+1):
    print(f"{i}.",ans[i-1])
