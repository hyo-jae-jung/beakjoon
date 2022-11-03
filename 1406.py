


""" false 1
sentence = input()
sentence=list(sentence)
N = len(sentence)
command_cnt = int(input())
command_list = (input() for _ in range(command_cnt))
cursor_position = N
for i in command_list:
    if i[0] == 'L' and cursor_position != 0: cursor_position-=1
    elif i[0] == 'D' and cursor_position != N: cursor_position+=1
    elif i[0] == 'B' and cursor_position != 0: 
        sentence.pop(cursor_position-1)
        N-=1
        cursor_position-=1
    elif i[0] =='P':
        sentence.insert(cursor_position,i[-1])
        N+=1
        cursor_position+=1

print(''.join(sentence))
"""

