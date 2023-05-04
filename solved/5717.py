from sys import stdin 
answer = []

while (temp:=stdin.readline().strip()) != '0 0':
    answer.append(sum(map(int,temp.split())))

print(*answer,sep='\n')
