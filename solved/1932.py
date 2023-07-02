from sys import stdin 

n = int(stdin.readline().strip())
triangle = []
for _ in range(n):
    triangle.append(list(map(int,stdin.readline().strip().split())))

for i in range(n-2,-1,-1):
    for j in range(i+1):
        triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1])

print(triangle[0][0])
        