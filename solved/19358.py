from sys import stdin   

z = int(stdin.readline().strip())
ans = []
for _ in range(z):
    n = int(stdin.readline().strip())
    tips = list(map(int,stdin.readline().strip().split()))
    tips.sort(reverse=True)
    for i in range(n):
        tips[i] = (tips[i] - i) if tips[i] >= i else 0
    ans.append(sum(tips))

print(*ans,sep='\n')
