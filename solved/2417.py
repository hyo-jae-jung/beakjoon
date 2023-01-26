from sys import stdin 

n = int(stdin.readline().strip())

import decimal 
temp = decimal.Decimal(str(n)).sqrt()
if temp%1==0:
    print(int(temp))
else:
    print(int(temp)+1)
