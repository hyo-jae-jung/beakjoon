M,N = map(int,input().split())
numbers_list = list(range(M,N+1))
T_or_F = [True]*len(numbers_list)
for j in range(2,int(N**0.5)+1):
    for i in numbers_list:
        if T_or_F[numbers_list.index(i)] == True:
            if i%j == 0 and i != j:
                T_or_F[numbers_list.index(i)] = False

for i in numbers_list:
    if T_or_F[numbers_list.index(i)] == True:
        print(i)