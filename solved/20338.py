from sys import stdin   

c,e,m = map(int,stdin.readline().strip().split())
ans = ["impossible"]
if c == 4 and e%2 == 0:
    left = 0
    right = e//2

    while left <= right:
        mid = (left+right)//2
        if mid*(e//2-mid) == m:
            ans = [mid+2,e//2-mid+2]
            break
        elif mid*(e//2-mid) < m:
            left = mid+1
        elif mid*(e//2-mid) > m:
            right = mid-1

print(*sorted(ans,reverse=True))
