from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    tmp = []
    n = int(stdin.readline().strip())
    i = 1
    while i < (n-i):
        tmp.append(str(i) + ' ' + str(n-i))
        i+=1
        
    ans.append("Pairs for {}: {}".format(n,', '.join(tmp)))

print(*ans,sep='\n')
