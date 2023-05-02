from sys import stdin 

V = int(stdin.readline().strip())
votes = list(stdin.readline().strip())
total = 0

while votes:
    temp = votes.pop()
    if temp == 'A':
        total+=1
    else:
        total-=1

if total > 0:
    print('A')
elif total < 0:
    print('B')
else:
    print('Tie')
