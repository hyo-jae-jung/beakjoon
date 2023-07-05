from sys import stdin 

N = int(stdin.readline().strip())

A,B,C = list(map(int,stdin.readline().strip().split()))

max_a,max_b,max_c = A,B,C
min_a,min_b,min_c = A,B,C
max_a,max_b,max_c,min_a,min_b,min_c
for _ in range(N-1):
    a,b,c = map(int,stdin.readline().strip().split())
    max_a,max_b,max_c = a + max(max_a,max_b),b + max(max_a,max_b,max_c),c + max(max_b,max_c)
    min_a,min_b,min_c = a + min(min_a,min_b),b + min(min_a,min_b,min_c),c + min(min_b,min_c)
    
print(max(max_a,max_b,max_c),min(min_a,min_b,min_c))
