from sys import stdin 

arr = []
for _ in range(7):
    arr.append(stdin.readline().strip().split())

print(sorted(arr,key=lambda x:(-int(x[1])))[0][0])
