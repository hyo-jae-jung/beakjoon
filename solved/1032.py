from sys import stdin 

N = int(stdin.readline().strip())
text_list = [stdin.readline().strip() for i in range(N)]

answer = []
for i in zip(*text_list):
    temp = set(i)
    if len(temp) == 1:
        answer.append(*temp)
    else:
        answer.append('?')

print(''.join(answer))
