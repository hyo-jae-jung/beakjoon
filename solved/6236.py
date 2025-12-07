from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
budget = [int(stdin.readline().strip()) for _ in range(N)]

def spend(budget,k):
    cnt = 0
    val = 0
    for i in budget:
        if val < i:
            cnt+=1
            val = k
        val-=i
    return cnt

left = max(budget)
right = sum(budget)

while left < right:
    mid = (left+right)//2
    if spend(budget,mid) > M:
        left = mid + 1
    else:
        right = mid

print(right)
