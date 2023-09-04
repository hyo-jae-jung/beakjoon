from sys import stdin 
print(int(stdin.readline().strip())-len(set(list(stdin.readline().strip().split()))))
