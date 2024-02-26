from sys import stdin 

N = int(stdin.readline().strip())

winners = []
for _ in range(N):
    winners.append(stdin.readline().strip())

d,p = 0,0

for i in winners:
    if i == 'D':
        d+=1
    else:
        p+=1
    
    if abs(d-p) == 2:
        break

print(f"{d}:{p}")
