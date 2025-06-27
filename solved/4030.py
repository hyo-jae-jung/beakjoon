from sys import stdin  
from bisect import bisect_left,bisect_right

i,j = 1,1
memo = []
b = 0
while (a:=i**2) <= 10**9:
    while a > b+1:
        b+=j
        j+=1
    if a == b+1:
        memo.append(a)
    i+=1

k = 1
ans = []
while (ab:=stdin.readline().strip()) != '0 0':
    a,b = map(int,ab.split())
    ans.append(f"Case {k}: {bisect_right(memo,b-1) - bisect_left(memo,a+1)}")
    k+=1
    
print(*ans,sep='\n')
