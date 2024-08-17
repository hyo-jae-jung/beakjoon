from sys import stdin 

N,M = map(int,stdin.readline().strip().split())

arr = [0]*M

for _ in range(M):
    A,B = map(int,stdin.readline().strip().split())
    arr[A-1][B-1]+=1
    arr[B-1][A-1]+=1 


for i in arr:
    print(sum(i))
