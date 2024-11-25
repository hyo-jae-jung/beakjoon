from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    arr = list(map(int,stdin.readline().strip().split()))
    a_arr = [arr[0]]
    for i in range(1,N):
        a_arr.append(a_arr[i-1]+arr[i])

    max_arg = -1000
    for i in range(N):
        tmp = a_arr[i]
        max_arg = max(max_arg,tmp)
        for j in range(0,i):
            max_arg = max(max_arg,tmp-a_arr[j])
    
    ans.append(max_arg)

print(*ans,sep='\n')
