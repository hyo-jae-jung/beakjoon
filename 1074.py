from sys import stdin 
from collections import deque

N,r,c = map(int,stdin.readline().strip().split())


def div(a:list)->list:
    answer = []
    answer.append(a[0:2])
    answer.append(a[2:4])
    return answer

def sum_h(a:list,b:list)->list:
    answer = []
    answer.append(a[0]+b[0])
    answer.append(a[1]+b[1])
    return answer

def sum_v(a:list,b:list)->list:
    return a + b

a0 = []
a1 = list(range(2**N*2**N))
a2 = []

def z(a:deque):
    i=0
    if len(a) == 4:
        return [a[:2],a[2:]]    
    else:
        temp = deque()
        while a:
            temp.append(a[i:i+4])
            
    return

if __name__ == "__main__":
    print(z([0,1,2,3]))
