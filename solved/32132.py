from sys import stdin  

N = int(stdin.readline().strip())
S = stdin.readline().strip()

ans = S[:2]
i,j = 2,2
for i in range(2,N):
    if ans[j-2:j] == 'PS' and S[i] in ('4','5'):
        continue
    else:
        ans+=S[i]
        j+=1

print(ans)
