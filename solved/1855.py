from sys import stdin 

K = int(stdin.readline().strip())
S = stdin.readline().strip()

step1 = ''
i = 0
while tmp:=S[K*i:K*(i+1)]:
    if i%2 != 0:
        tmp = reversed(tmp)
    step1+=''.join(tmp)
    i+=1

ans = ''

for i in range(K):
    for j in range(i,len(S),K):
        ans+=step1[j]

print(ans)
