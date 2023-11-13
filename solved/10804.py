from sys import stdin 

ans = list(range(1,21))
for _ in range(10):
    a,b = map(lambda x:int(x)-1,stdin.readline().strip().split())
    for i in range((b-a)//2+1):
        if a+i != b-i:
            ans[a+i],ans[b-i] = ans[b-i],ans[a+i]

print(*ans)
