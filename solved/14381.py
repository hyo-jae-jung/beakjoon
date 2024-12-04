from sys import stdin  

T = int(stdin.readline().strip())
ans = []

for i in range(1,T+1):
    N = int(stdin.readline().strip())
    if N == 0:
        ans.append(f"Case #{i}: INSOMNIA")
    else:
        nums = set()
        n = N
        flag = True
        while flag:
            for j in str(n):
                nums.add(j)
                if nums == set(map(str,list(range(10)))):
                    ans.append(f"Case #{i}: {n}")
                    flag = False
                    break
            n+=N

print(*ans,sep='\n')
