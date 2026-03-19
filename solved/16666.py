from sys import stdin 

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    k = int(stdin.readline().strip())
    A = list(map(int,stdin.readline().strip().split()))
    date_of_class = []
    for i in range(7):
        if A[i] == 1:
            date_of_class.append(i)
    result = float('inf')
    for i,j in enumerate(date_of_class,0):
        nk = k+i
        tmp = 7*(nk//len(date_of_class))
        tmp-=j

        if (r:=nk%len(date_of_class)):
            tmp+=date_of_class[r-1]+1
        else:
            tmp+=(date_of_class[-1]-6)
        result = min(result,tmp)
    ans.append(result)

print(*ans,sep='\n')
