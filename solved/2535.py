from sys import stdin 

N = int(stdin.readline().strip())
player = []
country = []
for _ in range(N):
    i,j,k = stdin.readline().strip().split()
    player.append((int(i),int(j),int(k)))
    country.append(int(i))

d = dict.fromkeys(set(country),0)

answer = []
player = sorted(player,key=lambda x:x[2])

while len(answer) < 3:
    temp=player.pop()
    if d[temp[0]] < 2:
        d[temp[0]]+=1
        answer.append(temp)

for i,j,_ in answer:
    print(i,j)
