from sys import stdin 

n = int(stdin.readline().strip())
s = stdin.readline().strip()

print((n-len(''.join(s.split('pPAp'))))//4)
