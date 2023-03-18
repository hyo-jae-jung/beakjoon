from sys import stdin 

# N,M = map(int,stdin.readline().strip().split())
# table = []
# for _ in range(N):
#     table.append(map(int,stdin.readline().strip()))

N,M = 4,3
table = ['112','305','678','654']

def square_num(x:str)->list:
    answer = []
    l = len(x)
    while l > 0:
        a=0
        b=l-a
        while b <= l:
            if isinstance(int(x[a:b])**0.5,int):
                answer.append(x[a:b])
            
    
    return