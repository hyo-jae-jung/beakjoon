from sys import stdin  

C = int(stdin.readline().strip())
ans = 0
for _ in range(C):
    t = stdin.readline().strip()
    tt = 0
    tt+=t.count('for')
    tt+=t.count('while')

    ans = max(tt,ans)

print(ans)
