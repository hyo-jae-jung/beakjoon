from sys import stdin  

N = int(stdin.readline().strip())
hp = []
weight = []
for _ in range(N):
    h,w = map(int,stdin.readline().strip().split())
    hp.append(h)
    weight.append(w)

ans = 0
def solution(idx=0,cnt=0):
    global N,hp,weight,ans

    if idx == N:
        ans = max(ans,cnt)
        return

    if hp[idx] <= 0:
        solution(idx+1,cnt)
        return

    for j in range(N):
        if hp[j] <= 0:
            solution(idx+1,cnt)
            continue

        if j != idx:
            hp[idx]-=weight[j]
            hp[j]-=weight[idx]
            solution(idx+1,cnt+(1 if hp[idx] <= 0 else 0)+(1 if hp[j] <= 0 else 0))
            hp[idx]+=weight[j]
            hp[j]+=weight[idx]

solution()
print(ans)
