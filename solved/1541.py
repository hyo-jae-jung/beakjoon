from sys import stdin 

string = stdin.readline().strip().split('-')

answer = 0
for i,j in enumerate(string):
    if i == 0:
        answer+=sum(map(int,j.split('+')))
    else:
        answer-=sum(map(int,j.split('+')))
        
print(answer)
