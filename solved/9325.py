from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    car_price = int(stdin.readline().strip())
    options_cnt = int(stdin.readline().strip())
    for _ in range(options_cnt):
        cnt,price = map(int,stdin.readline().strip().split())
        car_price+=cnt*price
    ans.append(car_price)

print(*ans,sep='\n')
