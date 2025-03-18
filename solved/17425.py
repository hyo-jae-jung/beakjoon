from sys import stdin   

T = int(stdin.readline().strip())
ans = []

LIMIT = 1_000_000

def sieve2(n):
    divisors_sum = [0 for _ in range(n+1)]
    for i in range(1,int(n**0.5)+1):
        for j in range(i,n+1,i):
            if int(j**0.5) >= i:
                divisors_sum[j]+=i
                if i != j//i:
                    divisors_sum[j]+=j//i

    return divisors_sum

div_s = sieve2(LIMIT)

prefix_s = [div_s[0]]
for i in range(1,LIMIT+1):
    prefix_s.append(prefix_s[-1]+div_s[i])

for _ in range(T):
    n = int(stdin.readline().strip())
    ans.append(prefix_s[n])

print(*ans,sep='\n')
