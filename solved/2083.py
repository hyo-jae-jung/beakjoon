from sys import stdin 
answer = []
while (s:=stdin.readline().strip()) != '# 0 0':
    name,age,kg = s.split()
    if int(age) > 17 or int(kg) >= 80:
        answer.append(name + ' ' +'Senior')
    else:
        answer.append(name + ' ' + 'Junior')

print(*answer,sep='\n')
