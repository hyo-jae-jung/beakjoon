from sys import stdin 

N = int(stdin.readline().strip())

candidates = []
for _ in range(N):
    candidates.append(int(stdin.readline().strip()))

cnt = 0
while True:
    first_idx = candidates.index(max(candidates))
    if first_idx == 0:
        if candidates.count(max(candidates)) > 1:
            cnt+=1
        break
    candidates[first_idx]-=1
    candidates[0]+=1
    cnt+=1

print(cnt)
