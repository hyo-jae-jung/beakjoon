from sys import stdin  

arr = [0,1]

for i in range(10):
    arr.append(arr[i]+arr[i+1])

print(arr)
