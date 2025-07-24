from sys import stdin   

T = int(stdin.readline().strip())
ans = []
for k in range(1,T+1):
    N = int(stdin.readline().strip())
    S = list(map(int,stdin.readline().strip().split()))

    odd_num = []
    odd_idx = []
    even_num = []
    even_idx = []

    for i,j in enumerate(S):
        if j%2 == 1:
            odd_num.append(j)
            odd_idx.append(i)
        else:
            even_num.append(j)
            even_idx.append(i)

    odd_idx.sort()
    even_idx.sort()

    odd_num.sort()
    even_num.sort(reverse=True)

    nums = [0]*N
    for i,j in zip(odd_idx,odd_num):
        nums[i] = j
    for i,j in zip(even_idx,even_num):
        nums[i] = j
    
    ans.append(f"Case #{k}: {' '.join(map(str,nums))}")

print(*ans,sep='\n')
