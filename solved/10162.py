from sys import stdin 

T = int(stdin.readline().strip())

def cook(t):
    
    answer = []
    for i in [300,60,10]:
        answer.append(t//i)
        t = t%i
    
    if t != 0:
        return [-1]
    else:
        return answer
    
print(*cook(T))
