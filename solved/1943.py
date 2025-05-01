from sys import stdin  

ans = []

def binary(n):
    i=0
    ans = []
    while n > (t:=2**i):
        ans.append(t)
        i+=1
        n-=t
    else:
        if n:
            ans.append(n)
    return ans

for _ in range(3):
    result = 0
    V,C = [],[]
    N = int(stdin.readline().strip())
    sumV = 0
    for _ in range(N):
        v,c = map(int,stdin.readline().strip().split())
        sumV+=v*c
        for i in binary(c):
            V.append(v*i)
            C.append(i)

    if sumV%2 == 0:
        dp = [1] + [0]*(sumV//2)
        for i in range(len(C)):
            if result == 0:
                for j in range(sumV//2,-1,-1):
                    if 0 <= j-V[i] <= sumV//2:
                        dp[j]+=dp[j-V[i]]
                        if dp[-1] > 0:
                            result = 1
                            break

    ans.append(result)
        
print(*ans,sep='\n')
