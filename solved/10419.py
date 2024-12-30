from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    d = int(stdin.readline().strip())
    i = 1
    while i+i**2 <= d:
        i+=1
    ans.append(i-1)

print(*ans,sep='\n')
