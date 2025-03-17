from sys import stdin  

d = int(stdin.readline().strip())

money = 100
my_shares = 0
stocks = []

for _ in range(d):
    stocks.append(int(stdin.readline().strip()))

for i in range(d-1):
    if my_shares == 0:
        if stocks[i+1] > stocks[i]:
            my_shares = (money//stocks[i]) if (money//stocks[i]) < 10**5 else 10**5
            money-=my_shares*stocks[i]
    if my_shares > 0:
        if stocks[i+1] < stocks[i]:
            money+=my_shares*stocks[i]
            my_shares = 0
else:
    if my_shares > 0:
        money+=my_shares*stocks[i+1]
        my_shares = 0

print(money)
