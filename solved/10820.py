import sys

sentence_list = []

while True:
    sentence = sys.stdin.readline()[:-1]
    if sentence != '':
        sentence_list.append(sentence)
    else:
        break

for i in sentence_list:
    d = dict.fromkeys(['lower','upper','num','empty'],0)
    for j in i:
        if j.islower():
            d['lower']+=1
        elif j.isupper():
            d['upper']+=1
        elif j == ' ':
            d['empty']+=1
        elif isinstance(int(j),int):
            d['num']+=1
    print(*d.values())
