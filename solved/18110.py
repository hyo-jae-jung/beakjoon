from sys import stdin 

def round(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(stdin.readline().strip())
if n:
    levs = []
    for _ in range(n):
        levs.append(int(stdin.readline().strip()))

    levs.sort()

    rm = round(n*0.15)
    
    answer = 0
    for i in range(rm,n-rm):
        answer+=levs[i]

    print(round(answer/(n-2*rm)))
else:
    print(0)
