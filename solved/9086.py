from sys import stdin 

T = int(stdin.readline().strip())
texts = []
for _ in range(T):
    texts.append(stdin.readline().strip())
    
answer = []

for i in texts:
    answer.append(i[0]+i[-1])

for i in answer:
    print(i)
