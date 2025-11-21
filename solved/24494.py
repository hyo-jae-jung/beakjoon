from sys import stdin  

grid1 = [list(stdin.readline().strip()) for _ in range(3)]
breeds = {}
for i in range(26):
    breeds.update({chr(65+i):0})

for i in range(3):
    for j in range(3):
        breeds[grid1[i][j]]+=1

green = 0
yellow = 0
guess = []
for i in range(3):
    for j,k in enumerate(stdin.readline().strip()):
        if grid1[i][j] == k:
            green+=1
            breeds[k]-=1
            continue
        guess.append(k)

for i in guess:
    if breeds[i] > 0:
        yellow+=1
        breeds[i]-=1

print(green)
print(yellow)
