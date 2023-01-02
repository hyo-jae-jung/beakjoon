from sys import stdin

N = int(stdin.readline().strip())

first = map(str,range(1,10))

def step(l:list,n:int)->list:

    def plma(x:str)->list:
        return [x+str(int(x[-1])-1),x+str(int(x[-1])+1)]

    sum_list = []

    for i in l:
        sum_list+=plma(i)
    return [i for i in sum_list if len(i)==n]


for i in range(N-1):
    first = step(first,i+2)

print(len(first))
