from sys import stdin 
from collections import defaultdict,deque 

T = int(stdin.readline().strip())

dictionary = defaultdict(str)

dictionary['@'] = '*3'
dictionary['%'] = '+5'
dictionary['#'] = '-7'

answer = []

for _ in range(T):
    temp = deque(stdin.readline().strip().split())
    sentence = temp.popleft()
    for i in temp:
        sentence = str(eval(sentence + dictionary[i]))
    answer.append(float(sentence))

for i in answer:
    print(f'{i:.2f}')
