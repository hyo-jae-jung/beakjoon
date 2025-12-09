from sys import stdin  

A,B,C = map(int,stdin.readline().strip().split())

binary = list(map(int,reversed(bin(B)[2:])))

arr = [A%C]
for _ in range(len(binary)-1):
    arr.append((arr[-1]**2)%C)

ans = 1
for i,j in enumerate(binary):
    if j == 1:
        ans = ans*arr[i]%C

print(ans)
