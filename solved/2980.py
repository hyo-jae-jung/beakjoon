from sys import stdin   

N,L = map(int,stdin.readline().strip().split())

total_waiting_time = 0
for _ in range(N):
    D,R,G = map(int,stdin.readline().strip().split())
    if (waiting_time := R - (D+total_waiting_time)%(R+G)) > 0 :
        total_waiting_time+=waiting_time
    
print(L+total_waiting_time)
