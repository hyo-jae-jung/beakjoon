from sys import stdin  

n,m = map(int,stdin.readline().strip().split())
trees = sorted(list(map(int,stdin.readline().strip().split())))
apples = sorted(list(map(int,stdin.readline().strip().split())))

ans = 10**8+1
i,j = 0,0
while i < n and j < m:
    ans = min(abs(trees[i] - apples[j]),ans)
    if trees[i] > apples[j]:
        j+=1
    elif trees[i] < apples[j]:
        i+=1
    else:
        break
    
print(ans)
