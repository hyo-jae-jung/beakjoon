from sys import stdin 
payment = int(stdin.readline().strip())
change = 1000 - payment
coin_cnt = 0
change_coins = [500,100,50,10,5,1]
for i in change_coins:
    coin_cnt+=change//i
    change=change%i

print(coin_cnt)
