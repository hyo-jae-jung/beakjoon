from sys import stdin  

m = int(stdin.readline().strip())
n = int(stdin.readline().strip())

cnt = 0
for j in range(2,3):
    for z in range(m+1):
        Z = z**j
        for y in range(z+1):
            Y = y**j
            for x in range(y+1):
                A = x**j + Y
                if A > Z:
                    break
                elif A == Z:
                    cnt+=1

print(cnt + (m+1)*(n-2))
