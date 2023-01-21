from sys import stdin 

inp = stdin.readline().strip()

answer = ''

for i in inp:
    if i.isupper():
        answer+=i.lower()
    else:
        answer+=i.upper()

print(answer)
