from sys import stdin 

N = int(stdin.readline().strip())
products = []
for _ in range(N):
    products.append(int(stdin.readline().strip()))

products.sort()

i = 1
ans = 0
while products:
    tmp = products.pop()
    if i != 3:
        ans+=tmp
        i+=1
    else:
        i = 1

print(ans)
