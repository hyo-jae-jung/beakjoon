import sys
from itertools import combinations as comb

def prime_numbers(a,b):
    answer = []
    T_or_F = [False]*2+[True]*len(range(2,b+1))

    for i in range(len(T_or_F)):
        if T_or_F[i]:
            for j in range(i*2,b+1,i):
                T_or_F[j] = False

    for i in range(a,b+1):
        if T_or_F[i]:
            answer.append(i)
    return answer

answer = []
while True:
    n = int(sys.stdin.readline().strip())
    if n!=0:
        answer.append([n,[i for i in comb(prime_numbers(1,n),2) if sum(i)==n][0]])
    else:
        break
    
for i in answer:
    print('{} = {} + {}'.format(i[0],i[1][0],i[1][1]))
