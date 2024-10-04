from sys import stdin  

w = stdin.readline().strip()

ans = "true"
for i in range(len(w)//2 + (1 if len(w)%2 else 0)):
    if w[i] != w[-1-i]:
        ans = "false"
        break

print(ans)
