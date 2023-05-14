from sys import stdin 

answer = []
while (sentence:=stdin.readline().strip()) !='END':
    answer.append(''.join(reversed(sentence)))

print(*answer,sep='\n')
