from sys import stdin  

N,X = map(int,stdin.readline().strip().split())  
arr = map(int,stdin.readline().strip().split())
print(0 if sum(arr)%X else 1)
