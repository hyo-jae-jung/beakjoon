N = int(input())
points = []
for _ in range(N):
    points.append(list(map(int,input().split())))

white_paper = [0]*10000

for i in points:
    for l in range(10):
        white_paper[(i[1]-1+l)*100+(i[0]-1):(i[1]-1+l)*100+(i[0]-1)+10] = [1]*10

print(sum(white_paper))
