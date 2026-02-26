from sys import stdin  

N = int(stdin.readline().strip())
S = stdin.readline().strip()

ans = N
prs = ['P','R','S']

for i in range(3):
    init = S.index(prs[i])
    cnt,prs_cnt = 0,0
    k = i
    for j in range(N+1):
        if S[(j+init)%N] == prs[k%3]:
            k+=1
            prs_cnt+=1
        if prs_cnt == 3:
            cnt+=1
            prs_cnt = 0

    ans = min(ans,N-cnt*3)

print(ans)
