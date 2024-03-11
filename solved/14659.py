from sys import stdin 

N = int(stdin.readline().strip())
mountains = list(map(int,stdin.readline().strip().split()))
ans = 0
j = 0
cnt = 0
for i in range(1,N):
    if mountains[j] > mountains[i]:
        cnt+=1
    elif mountains[j] < mountains[i]:
        ans = max(ans,cnt)
        cnt=0
        j = i
else:
    ans = max(ans,cnt)

print(ans)
