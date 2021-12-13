import math

A,B,C = map(int,input().split())

if B >= C:
    breat_even_point = -1
else:
    product_count = A/(C-B)
    if product_count%1 > 0:
        breat_even_point = math.ceil(product_count)
    else:
        breat_even_point = product_count + 1

print(int(breat_even_point))

