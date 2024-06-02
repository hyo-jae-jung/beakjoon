from sys import stdin  

N = int(stdin.readline().strip())

def evolution_cnt(k,m):
    cnt = 0
    while (m-k) >= 0:
        m-=(k-2)
        cnt+=1
    return cnt

ans = []
total_cnt = 0
for i in range(N):
    poketmon_name = stdin.readline().strip()
    K,M = map(int,stdin.readline().strip().split())
    cnt = evolution_cnt(K,M)
    total_cnt+=cnt
    ans.append((i,poketmon_name,cnt))

print(total_cnt)
print(sorted(ans,key=lambda x:(-x[2],x[0]))[0][1])
