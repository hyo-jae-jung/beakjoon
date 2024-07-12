from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n = int(stdin.readline().strip())
    total = 0
    for _ in range(n):
        product,ea,price = stdin.readline().strip().split()
        total+=int(ea)*float(price)

    ans.append(f"${total:.2f}")

print(*ans,sep='\n')
