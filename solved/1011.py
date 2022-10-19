import math

T = int(input())

data = []
for i in range(T):
    temp = []
    x, y = map(int,input().split())
    temp = [x,y]
    data.append(temp)

times_list = []

for i in data:
    d = i[1] - i[0]
    times = 0
    other_times = 0
    while (times+1)*(times+2) <= d:
        times += 1

    rest_of_distance = d - times*(times+1)

    if rest_of_distance != 0:
        for i in reversed(range(1,times+2)):
            other_times += rest_of_distance//i
            rest_of_distance = rest_of_distance%i
    
    total_times = times*2+other_times
    times_list.append(total_times)

for i in times_list:
    print(i)