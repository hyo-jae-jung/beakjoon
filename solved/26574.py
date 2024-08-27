from sys import stdin  

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    num = stdin.readline().strip()
    ans.append(num+" "+num)

print(*ans,sep='\n')
