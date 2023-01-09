from sys import stdin 

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
while a1:
    for _ in range(2):
        a2.append(a1[0:2])
        a1 = a1[2:]
    a0.append(a2)
    a2 = []

if __name__ == "__main__":
    print(list(a1))
    print(list(a2))
    print(list(a0))
