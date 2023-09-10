from sys import stdin 

N,W,H = map(int,stdin.readline().strip().split())

criteria = (W**2+H**2)**0.5
answer = []

for _ in range(N):
    matchstick = int(stdin.readline().strip())
    answer.append("DA" if criteria >= matchstick else "NE")

print(*answer,sep='\n')
