from sys import stdin  

N = int(stdin.readline().strip())
ans = 0
for _ in range(N):
    tmp = stdin.readline().strip()
    if '01' in tmp:
        ans+=1
        continue
    elif 'OI' in tmp:
        ans+=1

print(ans)
