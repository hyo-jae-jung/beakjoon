from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
table = list(stdin.readline().strip())

ans = 0
for i in range(N):
    if table[i] != 'X':
        for j in range(i-K if i >= K else 0,i+K+1 if i+K < N else N):
            if i != j:
                if table[i]+table[j] == 'HP' or table[i]+table[j] == 'PH':
                    table[i] = 'X'
                    table[j] = 'X'
                    ans+=1
                    break

print(ans)
