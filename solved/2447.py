from sys import stdin

N = int(stdin.readline().strip())

def stars(n):
    if n == 3:
        return ['***','* *','***']
    
    return [i*3 for i in stars(n//3)]+[i+' '*(n//3)+i for i in stars(n//3)]+[i*3 for i in stars(n//3)]

print(*stars(N),sep='\n')
