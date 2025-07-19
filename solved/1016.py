from sys import stdin  

a,b = map(int,stdin.readline().strip().split())

r = int((b**0.5))
prime_numbers = [1,1] + [0]*(r-1)

for i in range(2,r):
    for j in range(2*i,r+1,i):
        prime_numbers[j]+=1

l = [True]*(b-a+1)
for i,j in enumerate(prime_numbers):
    if j == 0:
        ii = i**2
        for k in range((a//ii+(1 if a%ii > 0 else 0))*ii-a,b-a+1,ii):
            l[k] = False

print(sum(l))
