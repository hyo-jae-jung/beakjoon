from sys import stdin  

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    tmp = list(map(int,stdin.readline().strip().split()))
    soldier_cnt = int(tmp[0])
    T = tmp[1:]
    d = {}
    for t in T:
        if not d.get(t):
            d.update({t:0})
        d[t]+=1
    
    data = sorted(d.items(),key=lambda x:x[1])
    if data[-1][1] > soldier_cnt//2:
        ans.append(data[-1][0])
    else:
        ans.append("SYJKGW")

print(*ans,sep='\n')
