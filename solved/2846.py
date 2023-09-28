from sys import stdin 

_ = stdin.readline()
arr = list(map(int,stdin.readline().strip().split()))

max_uphill = 0
start_loc = arr[0]

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        max_uphill = max(arr[i] - start_loc,max_uphill)
    else:
        start_loc = arr[i]

print(max_uphill)
