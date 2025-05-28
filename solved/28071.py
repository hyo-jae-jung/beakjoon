from sys import stdin  

N,M,K = map(int,stdin.readline().strip().split())
A = sorted(list(map(int,stdin.readline().strip().split())))

end = M*max(A)
dp = [1] + [0]*end

point = [(0,M)]

while point:
    idx,cnt = point.pop()
    if cnt > 0:
        for a in A:
            if dp[idx+a] == 0:
                dp[idx+a] = 1
                point.append((idx+a,cnt-1))

for i in range(end,-1,-1):
    if dp[i] and i%K == 0:
        print(i)
        break
