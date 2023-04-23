from sys import stdin 

N,M,B = map(int,stdin.readline().strip().split())

earth_met = []
for _ in range(N):
    earth_met.append(list(map(int,stdin.readline().strip().split())))

earth_arr = sum(earth_met,[])
    
max_floor = (sum(earth_arr)+B)//(N*M)
min_floor = 0
criterion_elapsed_time = sum((i-min_floor)*2 if i>min_floor else (min_floor-i) for i in earth_arr)
cnt = 0
while min_floor <= max_floor:
    mid = (max_floor+min_floor)//2
    comparison_elapsed_time = sum((i-mid)*2 if i>mid else (mid-i) for i in earth_arr)

    if comparison_elapsed_time <= criterion_elapsed_time:
        max_floor = mid - 1 
        criterion_elapsed_time = comparison_elapsed_time
    else:
        min_floor = mid + 1
    cnt+=1

print(criterion_elapsed_time,mid,cnt)
