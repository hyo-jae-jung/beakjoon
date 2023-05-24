from sys import stdin 
from collections import defaultdict

N = int(stdin.readline().strip())
chart = defaultdict(list)
for i in range(10):
    chart[chr(i+65)] = [0]*12

words_set = set([chr(i+65) for i in range(10)])
not_zero_words = set()
original = []
for _ in range(N):
    temp = stdin.readline().strip()
    original.append(temp)
    not_zero_words.add(temp[0])
    for i,j in zip(range(12),temp.rjust(12,'0')):
        if j != '0':
            chart[j][i]+=1

def diff_raise(x:list)->int:
    answer = 0
    for i,j in enumerate(reversed(x)):
        answer+=j*10**i
    return answer

zeroable = []
rest = []

for i in words_set^not_zero_words:
    zeroable.append((i,diff_raise(chart[i])))

zeroable.sort(key=lambda x:x[1])

zero = zeroable[0]
chart.pop(zero[0])

rest = []
for i,j in chart.items():
    rest.append((i,diff_raise(j)))
    
rest.sort(key=lambda x:x[1])

answer_chart = defaultdict(int)
for i,j in enumerate([zero]+rest):
    answer_chart[j[0]]=str(i)
answer = 0
for i in original:
    temp = ''
    for j in i:
        temp+=answer_chart[j]
    answer+=int(temp)

print(answer)
