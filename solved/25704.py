from sys import stdin  

N = int(stdin.readline().strip())
P = int(stdin.readline().strip())

discount_prices = [P,P-500,P*0.9,P-2000,P*0.75]

p = int(min(discount_prices[:1+N//5]))
print(0 if p < 0 else p)
