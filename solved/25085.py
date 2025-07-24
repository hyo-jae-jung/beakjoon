def check_palindrome(s):
    l = len(s)//2
    for i in range(l):
        if s[i] != s[-(i+1)]:
            return 0
    return 1

def factors(n):
    result = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            result.append(i)
            if n//i != i:
                result.append(n//i)
    return result

from sys import stdin   

ans = []
T = int(stdin.readline().strip())
A = []
for _ in range(T):
    A.append(int(stdin.readline().strip()))

for i,j in enumerate(A,1):
    ans.append(f"Case #{i}: {sum(check_palindrome(str(k)) for k in factors(j))}")

print(*ans,sep='\n')
