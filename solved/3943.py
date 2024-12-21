from sys import stdin  

T = int(stdin.readline().strip())

def heilstone(n):
    max_n = n
    while n != 1:
        if n%2==0:
            n = n//2
        else:
            n = n*3+1
        max_n = max(n,max_n)
    return max_n

ans = []
for _ in range(T):
    ans.append(heilstone(int(stdin.readline().strip())))

print(*ans,sep='\n')
