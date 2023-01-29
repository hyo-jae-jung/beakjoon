from sys import stdin 

N = int(stdin.readline().strip())

answer = []
for i in range(1,N+1):
    answer.append('Case #{}: {}'.format(i,' '.join(reversed(stdin.readline().strip().split()))))

for i in answer:
    print(i)
