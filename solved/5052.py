from sys import stdin 

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    n = int(stdin.readline().strip())
    nums = []
    for _ in range(n):
        nums.append(stdin.readline().strip())

    nums.sort()

    stats = True
    for i in range(1,n):
        if not stats:
            break

        if (l:=len(nums[i-1])) <= len(nums[i]):
            for j in range(l):
                if nums[i][j] != nums[i-1][j]:
                    break
            else:
                stats = False
    
    ans.append('YES' if stats else 'NO')

print(*ans,sep='\n')
