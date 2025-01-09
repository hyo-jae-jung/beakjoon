from sys import stdin  
import decimal

e = stdin.read().strip()
lines = e.splitlines()
ans = 0
for i in lines:
    ans+=decimal.Decimal(i)
print(f"{float(ans):.2f}")

