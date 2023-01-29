from sys import stdin 
from collections import deque 

answer = []
while True:
    message = stdin.readline().strip()
    if message == 'END':
        break
    alphabets = deque([i for i in list(message) if i != ' '])
    check_cnt = len(alphabets)
    while check_cnt > 0:
        check_alphabet = alphabets.popleft()
        if check_alphabet in alphabets:
            break
        alphabets.append(check_alphabet)
        check_cnt-=1
    else:
        answer.append(message)

print(*answer, sep='\n')
