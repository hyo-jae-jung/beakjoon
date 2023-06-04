from sys import stdin 
from math import ceil,floor,sqrt


gcd,lcm = map(int,stdin.readline().strip().split())

def getMyDivisor(n):
    divisorsList = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
    divisorsList.sort()
    return divisorsList

AB = lcm//gcd
A = getMyDivisor(AB)
print(A)
creteria = AB+1
left = 0
right = len(A)-1
while left<=right:
    mid = (left+right)//2
    a = A[mid]
    if creteria > a+AB//a:
        left = mid+1
    else:
        right = mid-1
    creteria = a+AB//a
else:
    print(gcd*A[mid],gcd*AB//A[mid])
