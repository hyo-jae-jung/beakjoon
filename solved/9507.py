from sys import stdin  

t = int(stdin.readline().strip())
memo = [0]*68

def koong(n):

    if memo[n]:
        return memo[n]
    if n < 2:
        memo[n] = 1
    elif n == 2:
        memo[n] = 2
    elif n == 3:
        memo[n] = 4
    elif n > 3:
        memo[n] = koong(n-1)+koong(n-2)+koong(n-3)+koong(n-4)

    return memo[n]
    
ans = []
for i in range(t):
    ans.append(koong(int(stdin.readline().strip())))

print(*ans,sep='\n')

