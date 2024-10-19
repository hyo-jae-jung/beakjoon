from sys import stdin  

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    ans.append(max(map(int,stdin.readline().strip().split())))

for i,j in enumerate(ans,1):
    print(f"Case #{i}: {j}")
    