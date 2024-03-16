from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for i in map(int,stdin.readline().strip().split()):
    s = 0
    n3 = i//3
    n7 = i//7
    n21 = i//21

    ans.append(3*n3*(n3+1)//2 + 7*n7*(n7+1)//2 - 21*n21*(n21+1)//2)

print(*ans, sep='\n')
