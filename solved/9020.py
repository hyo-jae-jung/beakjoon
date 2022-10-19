import sys

T = int(sys.stdin.readline())
even_numbers_list = []
for i in range(T):
    even_numbers_list.append(int(sys.stdin.readline().strip()))

max_N = max(even_numbers_list)

T_or_F = [False]*2 + [True]*len(range(2,max_N+1))

for i in range(len(T_or_F)):
    if T_or_F[i]:
        for j in range(i*2,max_N+1,i):
            T_or_F[j] = False


goldbach_partitions_list = []
for h in even_numbers_list:
    goldbach_number = h
    goldbach_partition_samples_list = []
    for i in range(2,int(goldbach_number/2)+1):
        goldbach_partition = []
        if T_or_F[i] and T_or_F[goldbach_number-i]:
            goldbach_partition.append(i)
            goldbach_partition.append(goldbach_number-i)
            goldbach_partition_samples_list.append(goldbach_partition)

    goldbach_partitions_list.append(goldbach_partition_samples_list[-1])

for i in goldbach_partitions_list:
    print(f"{i[0]} {i[1]}")