from sys import stdin  

n = int(stdin.readline().strip())

if '7' in str(n):
    is_contained = True
else:
    is_contained = False

if n%7 == 0:
    is_divisible = True
else:
    is_divisible = False

if is_contained and is_divisible:
    print(3)
elif is_contained and is_divisible == False:
    print(2)
elif is_contained == False and is_divisible:
    print(1)
else:
    print(0)
