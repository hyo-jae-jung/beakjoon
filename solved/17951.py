from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
paper = list(map(int,stdin.readline().strip().split()))

left = 1
right = sum(paper)
prefix_sum = [0]
for i in paper:
    prefix_sum.append(prefix_sum[-1]+i)


while left < right:

    mid = (left+right)//2 + (1 if (left+right)%2 > 0 else 0)
    g = 0
    i,j = 0,1
    a = []
    while i+j <= N:
        t = prefix_sum[i+j] - prefix_sum[i]
        if t >= mid:
            g+=1
            a.append(t)
            i+=j
            j = 1
        else:
            j+=1
    else:
        if i < N:
            if prefix_sum[-1] - prefix_sum[i] >= mid:
                g+=1
                a.append(prefix_sum[-1] - prefix_sum[i])
            else:
                a[-1]+=prefix_sum[-1] - prefix_sum[i]

    if g >= K:
        left = mid
    else:
        right = mid - 1

print(right)
