from sys import stdin 

word_list = []
while True:
    temp = stdin.readline().strip()
    if temp == '-':
        break
    word_list.append(temp)

box_list = []
while True:
    temp = stdin.readline().strip()
    if temp == '#':
        break
    box_list.append(temp)

def check_essential_alphabet(essential_alphabet:str,word_list:list)->list:
    answer = []
    for i in word_list:
        if essential_alphabet in i:
            answer.append(i)
    return answer

def check_subset(box:str,word_list:list)->list:
    from copy import copy
    answer = []
    for i in word_list:
        sample_box = list(box)
        for j in i:
            try:
                sample_box.remove(j)
            except:
                break
        else:
            answer.append(i)
    return answer

for box in box_list:
    set_box = set(box)
    cnt_d = dict()
    for alphabet in set_box:
        a = check_essential_alphabet(alphabet,word_list)
        b = check_subset(box,a)
        cnt_d[alphabet] = len(b)

    cnt = []
    for i,j in cnt_d.items():
        cnt.append((i,j))

    cnt.sort(key=lambda x:x[1])

    min_cnt = cnt[0][1]
    max_cnt = cnt[-1][1]

    min_alphabet = ''
    max_alphabet = ''

    cnt.sort(key=lambda x:x[0])

    for i,j in cnt:
        if j == min_cnt:
            min_alphabet+=i
        if j == max_cnt:
            max_alphabet+=i

    print(min_alphabet,min_cnt,max_alphabet,max_cnt)
