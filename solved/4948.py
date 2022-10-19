import sys

N_list = []
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    else:
        N_list.append(N)

T_or_F = [False]*2+[True]*len(range(2,2*max(N_list)+1))

for i in range(len(T_or_F)):
    if T_or_F[i]:
        for j in range(i*2,2*max(N_list)+1,i):
            T_or_F[j] = False
for i in N_list:
    prime_number_count = 0
    for j in range(i+1,2*i+1):
        if T_or_F[j]:
            prime_number_count += 1
    print(prime_number_count)