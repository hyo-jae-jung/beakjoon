from sys import stdin 

T = int(stdin.readline().strip())

answer = []

def which_triangle(l):
    l.sort()
    if l[0] == l[-1]:
        return 'equilateral'
    if (l[0]+l[1]) <= l[-1]:
        return 'invalid!'
    if len(set(l)) == 2:
        return 'isosceles'
    else:
        return 'scalene'

for i in range(1,T+1):
    abc = list(map(int,stdin.readline().strip().split()))
    answer.append(f'Case #{i}: {which_triangle(abc)}')

print(*answer,sep='\n')
