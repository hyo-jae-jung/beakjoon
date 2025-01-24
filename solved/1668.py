from sys import stdin  

N = int(stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(int(stdin.readline().strip()))

A = arr[0]
a_cnt = 1
for i in range(1,N):
    if arr[i] > A:
        a_cnt+=1
        A = arr[i]

B = arr[-1]
b_cnt = 1
for i in range(N-1,-1,-1):
    if arr[i] > B:
        b_cnt+=1
        B = arr[i]

print(a_cnt)
print(b_cnt)
