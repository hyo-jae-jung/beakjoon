from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
ans = []
for _ in range(M):
    A = list(map(int,stdin.readline().strip().split()))
    zero = False
    minus_arr = []
    plus = 0
    for a in A:
        if a > 0:
            if plus == 0:
                plus+=1
            plus*=a
        elif a < 0:
            minus_arr.append(a)
        elif a == 0:
            zero = True

    minus_arr.sort()
    minus = 1
    for i in minus_arr if len(minus_arr)%2 == 0 else minus_arr[:-1]:
        minus*=i
    
    
    if plus == 0:
        if zero:
            if len(minus_arr) <= 1:
                ans.append(0)
            else:
                ans.append(minus)
        else:
            if len(minus_arr) <= 1:
                ans.append(minus_arr[-1])
            else:
                ans.append(minus)
    else:
        ans.append(plus*minus)
        
print(*ans,sep='\n')
