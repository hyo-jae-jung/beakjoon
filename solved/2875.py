from sys import stdin 

N,M,K = map(int,stdin.readline().strip().split())

N_val = N//2
N_rest = N - N_val
max_mean_cnt = min(M,N_val)

total_rest = N + M - max_mean_cnt*(2 + 1)

K-=total_rest

if K > 0:
    k_val,k_rest = K//3,K%3
    tmp = max_mean_cnt - k_val - (1 if k_rest else 0)
    print(tmp if tmp > 0 else 0)
else:
    print(max_mean_cnt)
    