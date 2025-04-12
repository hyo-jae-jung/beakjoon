from sys import stdin  
from bisect import bisect_left

N = int(stdin.readline().strip())
liquid = sorted(list(map(int,stdin.readline().strip().split())))

ans = [10**9,10**9]

for i in range(N):

    j = bisect_left(liquid,-liquid[i])

    if j == N or abs(liquid[i]+liquid[j-1]) < abs(liquid[i]+liquid[j]):
        j-=1

    if i == j:
        continue

    ans = ans if abs(sum(ans)) < abs(liquid[i]+liquid[j]) else [liquid[i],liquid[j]]

    if sum(ans) == 0:
        break

print(*sorted(ans))

