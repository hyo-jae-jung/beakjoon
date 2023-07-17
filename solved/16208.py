from sys import stdin 
n = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
A.sort()

sum_A = sum(A)
answer = 0
for i in A:
    sum_A-=i
    answer+=i*sum_A

print(answer)
