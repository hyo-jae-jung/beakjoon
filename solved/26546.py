from sys import stdin  

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    s,i,j = stdin.readline().strip().split()
    tmp = ''
    for k in range(len(s)):
        if k < int(i) or int(j) <= k:
            tmp+=s[k]

    ans.append(tmp)

print(*ans,sep='\n')
