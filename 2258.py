from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
meets = []
for _ in range(N):
    meets.append(list(map(int,stdin.readline().strip().split())))

meets.sort(key=lambda x:x[1])

print(*meets,sep='\n')

for i in range(1,len(meets)):
    meets[i][0]+=meets[i-1][0]
print(*meets,sep='\n')


