from sys import stdin 

N = int(stdin.readline().strip())
ans = []
for j in range(1,N+1):
    S = int(stdin.readline().strip())
    d = {}
    for i in range(S):
        d.update({stdin.readline().strip():i})

    Q = int(stdin.readline().strip())
    tmp = 0
    switch_cnt = 0
    for _ in range(Q):
        engine_id = d[stdin.readline().strip()]
        if (tmp | (1 << engine_id)) == ((1 << S) - 1):
            tmp = (1 << engine_id)
            switch_cnt+=1
        else:
            tmp |= (1 << engine_id)
    ans.append(f"Case #{j}: {switch_cnt}")

print(*ans,sep='\n')
