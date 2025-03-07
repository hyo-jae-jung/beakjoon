from sys import stdin   

N = int(stdin.readline().strip())
cows = list(map(int,stdin.readline().strip().split()))

cows.sort(reverse=True)

w_cnt = 0
for i in cows:
    if i >= w_cnt:
        w_cnt+=1

print(w_cnt)
