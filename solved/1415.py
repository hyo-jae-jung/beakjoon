from sys import stdin  

N = int(stdin.readline().strip())
candies = {}
max_price = 0
zero_cnt = 0
for _ in range(N):
    candy = int(stdin.readline().strip())
    if candy > 0:
        max_price+=candy
        if not candies.get(candy):
            candies.update({candy:0})
        candies[candy]+=1
    else:
        zero_cnt+=1

dp = [1] + [0]*max_price
for price,count in candies.items():
    for i in range(max_price,-1,-1):
        for j in range(count,0,-1):
            if 0 <= i+price*j <= max_price:
                dp[i+price*j]+=dp[i]

ans = 0

prime_numbers = []
check_numbers = [0]*(max_price+1)
for i in range(2,int(max_price**0.5)+1):
    for j in range(i+1,max_price+1):
        check_numbers[j]+= 1 if j%i == 0 else 0

for i,j in enumerate(check_numbers[2:],2):
    if j == 0:
        ans+=dp[i]

print(ans*(zero_cnt+1))
