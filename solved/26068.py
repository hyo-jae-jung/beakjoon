from sys import stdin  

N = int(stdin.readline().strip())
ans = 0
for _ in range(N):
    _,num = stdin.readline().strip().split("-")
    if int(num) <= 90:
        ans+=1

print(ans)
