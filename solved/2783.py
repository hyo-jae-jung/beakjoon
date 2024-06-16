from sys import stdin 

X,Y = map(int,stdin.readline().strip().split())
ans = (1000/Y)*X

for _ in range(int(stdin.readline().strip())):
    x,y = map(int,stdin.readline().strip().split())
    ans = min(ans,(1000/y)*x)

print(f"{ans:.2f}")
