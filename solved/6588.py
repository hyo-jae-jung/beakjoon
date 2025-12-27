from sys import stdin   

N = 1_000_000
arr = [True]*(N+1)

for i in range(2,int(N**0.5)+1):
    if arr[i]:
        for j in range(2*i,N+1,i):
            arr[j] = False

for i in range(3):
    arr[i] = False

prime_numbers = []
for i,j in enumerate(arr):
    if j:
        prime_numbers.append(i)

ans = []
while (n:=int(stdin.readline().strip())) != 0:
    tmp = "Goldbach's conjecture is wrong."

    for prime_number in prime_numbers:
        if n < prime_number + 3:
            break

        if arr[n-prime_number]:
            tmp = f"{n} = {prime_number} + {n-prime_number}"
            break

    ans.append(tmp)

print(*ans,sep='\n')
