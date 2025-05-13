from sys import stdin  

arr = [1,1]
for i in range(2,251):
    arr.append(arr[i-1] + arr[i-2]*2)

e = stdin.read().strip()
lines = e.splitlines()

for i in lines:
    print(arr[int(i)])
    