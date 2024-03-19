from sys import stdin 

S = list(map(ord,list(stdin.readline().strip())))

ans = 1
for i in range(1,len(S)):
    if S[i] <= S[i-1]:
        ans+=1

print(ans)
