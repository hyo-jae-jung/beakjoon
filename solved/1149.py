from sys import stdin 

N = int(stdin.readline().strip())
painting_costs = []
for _ in range(N):
    painting_costs.append(list(map(int,stdin.readline().strip().split())))

for i in range(1,N):
    painting_costs[i][0]+=min(painting_costs[i-1][1],painting_costs[i-1][2])
    painting_costs[i][1]+=min(painting_costs[i-1][0],painting_costs[i-1][2])
    painting_costs[i][2]+=min(painting_costs[i-1][0],painting_costs[i-1][1])

print(min(painting_costs[-1]))
