from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    a,b = stdin.readline().strip().split()
    ans.append(bin(int(a,2) + int(b,2))[2:])

print(*ans,sep='\n')
