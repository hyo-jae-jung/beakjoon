from sys import stdin 

N = int(stdin.readline().strip())
A = [int(i) for i in stdin.readline().strip().split()]

A.sort()

left = 0
right = N-1
temp = sum(abs(i-A[left]) for i in A)
while left<right:
    mid = (left+right)//2
    temp2 = sum(abs(i-A[mid]) for i in A)

    if temp2 < temp:
        