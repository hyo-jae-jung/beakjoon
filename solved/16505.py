from sys import stdin  

N = int(stdin.readline().strip())
arr = ['*']
for i in range(N):
    tmp = []
    for j in range(2**i):
        tmp.append(arr[j]*2)
    
    for j in range(2**i):
        tmp.append(arr[j] + ' '*(2**i))

    arr = tmp

for i in arr:
    print(i.strip())
