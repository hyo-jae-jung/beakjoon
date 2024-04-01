from sys import stdin  

S = stdin.readline().strip()

ans = 0

for i,j in enumerate(reversed(S)):
    ans+=(26**i)*(ord(j)-64)

print(ans)
