from sys import stdin 
from math import gcd,lcm 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    a,b = map(int,stdin.readline().strip().split())
    answer.append((lcm(a,b),gcd(a,b)))

for i in answer:
    print(*i)
