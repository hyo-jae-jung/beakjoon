from sys import stdin   

T = int(stdin.readline().strip())
ans = []

for _ in range(T):
    N,K = map(int,stdin.readline().strip().split())
    candy_cnt = list(map(int,stdin.readline().strip().split()))
    child_cnt = 0
    for i in candy_cnt:
        child_cnt+=i//K
    ans.append(child_cnt)

print(*ans,sep='\n')
