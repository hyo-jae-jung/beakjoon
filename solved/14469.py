from sys import stdin 

N = int(stdin.readline().strip())
cows = []
for _ in range(N):
    cows.append(tuple(int(i) for i in stdin.readline().strip().split()))

cows.sort(key=lambda x:(x[0],x[1]))

total_time = 0
for i,j in cows:
    if total_time > i:
        total_time+=j
    else:
        total_time = i+j

print(total_time)
