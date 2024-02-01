from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    nums = [int(i) for i in map(lambda x:int(x) if int(x)%2 == 0 else 0,stdin.readline().strip().split()) if i]
    ans.append((sum(nums),min(nums)))

for i in ans:
    print(*i)
    