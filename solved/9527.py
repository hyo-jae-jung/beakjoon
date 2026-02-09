from sys import stdin  

A,B = map(int,stdin.readline().strip().split())
dp = [0]*55
for i in range(54):
    dp[i+1] = 2*dp[i] + (1 << i)

def solution(num):
    global dp
    val,cnt = 0,0
    while num > 0:
        i = len(bin(num))-3
        val+=(cnt*(2**i) + dp[i])
        num-=2**i
        cnt+=1
    return val

print(solution(B+1) - solution(A))
