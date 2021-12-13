N = int(input())
n = 0
while N > n*(n+1)/2:
    n += 1

if n%2 == 1 :
    print(f"{int(1+(n*(n+1)/2-N))}/{int(n-(n*(n+1)/2-N))}")
else:
    print(f"{int(n-(n*(n+1)/2-N))}/{int(1+(n*(n+1)/2-N))}")