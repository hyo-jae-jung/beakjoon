from sys import stdin 

answer = int(stdin.readline().strip())
for _ in range(9):
    answer-=int(stdin.readline().strip())

print(answer)
