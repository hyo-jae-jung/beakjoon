from sys import stdin 

N,K = map(int,stdin.readline().strip().split())
arr = [int(i) for i in stdin.readline().strip().split(',')]

while K > 0:
    tmp = []
    for i in range(1,len(arr)):
        tmp.append(arr[i]-arr[i-1])
    arr = tmp
    K-=1

print(','.join(map(str,arr)))
