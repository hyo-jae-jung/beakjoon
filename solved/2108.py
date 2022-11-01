import sys

N = int(sys.stdin.readline().strip())
num_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

avg = round(sum(num_list)/len(num_list))

count = dict()
sorted_arr = list()

for i in num_list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in sorted(count.keys()):
    for _ in range(count[i]):
        sorted_arr.append(i)

if len(sorted_arr)%2==0:
    median = sum(sorted_arr[len(sorted_arr)-1:len(sorted_arr)+1])/2
else:
    median = sorted_arr[len(sorted_arr)//2]

temp = [i[0] for i in count.items() if i[1]==max(count.values())]
if len(temp)<=1:
    mode = temp[0]
else:
    temp.sort()
    mode = temp[1]

coverage = max(num_list) - min(num_list)

print(avg)
print(median)
print(mode)
print(coverage)
