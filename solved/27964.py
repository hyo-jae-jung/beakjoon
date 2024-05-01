from sys import stdin 
N = int(stdin.readline().strip())
topping = list(stdin.readline().strip().split())

s = set()

for i in topping:
    if i not in s and i[-6:] == 'Cheese':
        s.add(i)
        
print('yummy' if len(s) >= 4 else 'sad')
