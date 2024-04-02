from sys import stdin 

S = stdin.readline().strip()

ans = 0

a = S[0]
cnt = 1
for i in range(1,len(S)):
    if int(S[i]) == int(a) + 1:
        cnt+=1
    else:
        if cnt == 3:
            ans+=1
        cnt = 1

    a = S[i]
else:
    if cnt == 3:
        ans+=1

print(ans)
