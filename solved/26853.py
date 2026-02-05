from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
ans = 0
words = [stdin.readline().strip() for _ in range(N)]

for i in range(M):
    d = {}
    for j in range(N):
        if not d.get(words[j][i]):
            d.update({words[j][i]:0})
        d[words[j][i]]+=1
    ans+=(N - max(d.values()))

print(ans)
