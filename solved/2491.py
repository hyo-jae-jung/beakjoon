from sys import stdin  

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))

ans = 1
left,right = [],[]
for i in range(N):
    if not left:
        left.append(arr[i])
    else:
        if left[-1] >= arr[i]:
            left.append(arr[i])
        else:
            ans = max(ans,len(left))
            left = [arr[i]]

    if not right:
        right.append(arr[i])
    else:
        if right[-1] <= arr[i]:
            right.append(arr[i])
        else:
            ans = max(ans,len(right))
            right = [arr[i]]
else:
    ans = max(ans,len(left),len(right))

print(ans)
