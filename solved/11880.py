from sys import stdin
T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    a,b,c = map(int,stdin.readline().strip().split())
    answer.append(min((a+b)**2+c**2,(a+c)**2+b**2,(b+c)**2+a**2))

print(*answer,sep='\n')
