from sys import stdin 

N = int(stdin.readline().strip())
students = list(map(int,stdin.readline().strip().split()))
ans = 0
for i in range(N):
    if i+1 != students[i]:
        ans+=1

print(ans)
