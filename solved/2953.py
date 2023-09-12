from sys import stdin 

total_scores = []
for i in range(1,6):
    total_scores.append((i,sum(map(int,stdin.readline().strip().split()))))

total_scores.sort(key=lambda x:-x[1])
print(*total_scores[0])
