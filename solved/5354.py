from sys import stdin  

n = int(stdin.readline().strip())

ans = []

for _ in range(n):
    tmp = int(stdin.readline().strip())
    t = []
    for i in range(tmp):
        if i == 0 or i == tmp-1:
            t.append("#"*tmp)
        else:
            t.append("#"+"J"*(tmp-2)+"#")
    
    ans.append(t)

for k,i in enumerate(ans,1):
    for j in i:
        print(j)
    if k != n:
        print()
