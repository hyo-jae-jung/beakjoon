from sys import stdin 

answer = []
while True:
    temp = stdin.readline().strip().split()
    if not all(map(int,temp)):
        break
    L,P,V = map(int,temp)
    answer.append(L*(V//P) + (V%P if V%P <=L else L))

for i,j in enumerate(answer,1):
    print(f'Case {i}: {j}')
    