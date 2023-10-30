from sys import stdin 

ate = 0
mushrooms = []
for _ in range(10):
    mushrooms.append(int(stdin.readline().strip()))

for mushroom in mushrooms:
    if ate + mushroom >= 100:
        a = abs(100-ate)
        b = abs(100-ate-mushroom)
        if a == b:
            print(ate+mushroom)
        elif a > b:
            print(ate+mushroom)
        elif a < b:
            print(ate)
        break
    else:
        ate+=mushroom
else:
    print(ate)
