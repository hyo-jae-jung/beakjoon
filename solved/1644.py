from sys import stdin 

N = int(stdin.readline().strip())

sieve = [True]*(N+1)
m = int(N**0.5)
for i in range(2,m+1):
    if sieve[i] == True:
        for j in range(i+i,N+1,i):
            sieve[j] = False

prime_nums = [i for i in range(2,N+1) if sieve[i] == True]

left = 0
right = 0
hab = 0
cnt = 0
prime_nums+=[0]

while right < len(prime_nums):
    if hab == N:
        cnt+=1
        hab-=prime_nums[left]
        left+=1
    elif hab > N:
        hab-=prime_nums[left]
        left+=1
    elif hab < N:
        hab+=prime_nums[right]
        right+=1

print(cnt)

if __name__ =="__main__":
    print(prime_nums)
