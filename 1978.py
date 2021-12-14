N = int(input())
numbers = list(map(int,input().split()))
Prime_Numbers_count = 0

try:
    for _ in numbers:
        numbers.remove(1)
except:
    pass

try:
    while 2 in numbers:
        numbers.remove(2)
        Prime_Numbers_count += 1
except:
    pass

for i in numbers:
    temp_count = 0
    for j in range(2,i):
        if i%j == 0:
            temp_count += 1
    if temp_count == 0:
        Prime_Numbers_count += 1

print(Prime_Numbers_count)