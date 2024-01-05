from sys import stdin 

ans = []
for _ in range(int(stdin.readline().strip())):
    INPUT = stdin.readline().strip()
    ans.append(INPUT[0].upper() + INPUT[1:])

print(*ans, sep='\n')
