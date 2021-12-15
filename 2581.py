M=int(input())
N=int(input())
numbers_list = list(range(M,N+1))
prime_numbers_list = []

for i in numbers_list:
    if i == 1:
        continue
    elif i == 2:
        prime_numbers_list.append(i)
    else:
        temp_count = 0
        for j in range(2,i):
            if i%j == 0:
                temp_count += 1
                break
        if temp_count == 0:
            prime_numbers_list.append(i)

if len(prime_numbers_list) == 0:
    print(-1)
else:
    print(sum(prime_numbers_list))
    print(min(prime_numbers_list))
