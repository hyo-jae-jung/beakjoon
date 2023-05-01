from sys import stdin 

N = int(stdin.readline().strip())
answer = []
for _ in range(N):
    r,e,c = map(int,stdin.readline().strip().split())
    calculate_costs = e-c-r
    if calculate_costs > 0:
        answer.append('advertise')
    elif calculate_costs < 0:
        answer.append('do not advertise')
    else:
        answer.append('does not matter')

print(*answer,sep='\n')
    