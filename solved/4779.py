from sys import stdin 

def cantor(n):
    if n == 0:return '-'
    return cantor(n-1) + ' '*3**(n-1) + cantor(n-1)

answer = []

while (N := stdin.readline().strip()) != '':
    answer.append(cantor(int(N)))
    
print(*answer,sep='\n')
