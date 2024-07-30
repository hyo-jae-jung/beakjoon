from sys import stdin 

L = int(stdin.readline().strip())

print(L//5 + (1 if L%5 > 0 else 0))
