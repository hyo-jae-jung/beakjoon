from sys import stdin 

ns = []
while True:
    temp = int(stdin.readline().strip())
    if temp != -1:
        ns.append(temp)
    else:
        break

def aliquot(num:int)->list:
    answer = []
    for i in range(1,int(num**0.5)+1):
        if num%i == 0:
            answer.append(i)
            if num//i not in answer:
                answer.append(num//i)
    answer.sort()
    return answer

def is_perfect_num(x:list)->str:
    answer = ''
    if x[-1] == sum(x[:-1]):
        answer = '{} = {}'.format(x[-1],' + '.join(map(str,x[:-1])))
    else:
        answer = f'{x[-1]} is NOT perfect.'
    return answer

for i in ns:
    print(is_perfect_num(aliquot(i)))
    